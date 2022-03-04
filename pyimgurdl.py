
import os
import sys
from typing import Callable
from requests_html import HTMLSession
def download_imgur(url: str, dl_path: str, max_width=2160, print_fn:Callable=print):
    """Download images from imgur album
        (e.g. https://imgur.com/a/XXXXXX or https://imgur.com/gallery/XXXXXX)\n
        Works with NSFW albums which cannot be parsed directly because of the "This post may contain erotic or adult imagery" warning
        :param url: Url of imgur album
        :param dl_path: Path to save those images 
        :param max_width: Maximum width of image to be downloaded, defaults to be 2160
        :param print_fn Function Callable[str] to print log, can be None
    """
    with HTMLSession() as session:
        real_url = url
        try:
            r = session.get(f'{url}/embed', headers={'Content-Type': 'text/html;charset=utf-8'})
            for img in r.html.find('ul li img'):
                img = 'https:' + img.attrs['data-src']
                real_url = img.replace('s.jpg', f'_d.webp&fidelity=grand&maxwidth={max_width}')
                file = session.get(real_url)
                file_name = os.path.basename(img).replace('s.jpg','.webp')
                fullpath = os.path.join(dl_path, file_name)
                with open(fullpath, 'wb') as f:
                    f.write(file.content)
                    f.flush()
                if print_fn is not None:
                    print_fn(f'imgur: Download "{file_name}" from {real_url} (base: {url})')
        except Exception as e:
            if print_fn is not None:
                print_fn(f'imgur: failed to download {real_url}, exception: {e}')
            raise e
        
def main():
    try:
        url = sys.argv[1]
        if not url.startswith('https://imgur.com'):
            print(f'Invalid URL: {url}, format: "https://imgur.com/..."')
            raise
        dl_path = sys.argv[2]
        if not os.path.exists(dl_path):
            print(f'Directory "{dl_path}" does not exist.')
            raise
        download_imgur(url, dl_path)
    except:
        print(
'''Usage: python -m pyimgurdl [URL] [SAVE_PATH]
    Arguments:
        URL: url of imgur album (e.g. https://imgur.com/a/XXXXXX or https://imgur.com/gallery/XXXXXX)
        SAVE_PATH: path to save the downloaded images (The path MUST exists)
''')
        
if __name__ == '__main__':
    main()