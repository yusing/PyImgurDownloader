# PyImgurDownloader - A Python Imgur downloader module

## About The Project

This is a simple Python script to download images from imgur album

Works with *NSFW albums* which cannot be parsed directly using `request.get()` because of the "This post may contain erotic or adult imagery" warning

## Prerequisites

Simpliy clone this repository
Run `pip install -r requirements.txt` to install required dependencies

## Class Usage

```python
download_imgur('https://imgur.com/a/ALR5Kbg', dl_path: 'C:\Users\user\Pictures\imgur')
```

## Command Line Usage

`python -m pyimgurdl [URL] [SAVE_PATH]`  
`URL` url of imgur album (e.g. <https://imgur.com/a/ALR5Kbg> or <https://imgur.com/gallery/ALR5Kbg>)  
`SAVE_PATH` path to save the downloaded images (**MUST** exists)  

## License

MIT