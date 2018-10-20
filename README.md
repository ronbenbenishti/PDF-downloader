# PDF-downloader
Scan and download all .PDF files from digitalwhisper.co.il

## Features: ##
* Dealing with duplicate files
* Progress bar
* All links are saved in *'links.txt'* file.
* Verification: Downloaded file size matches the original file size


## Prerequisites: ##
* python 2.7
* Modules in use:
  * BeautifulSoup (bs4)
  * urllib
  * urllib2
  * progress
  
## Installing ##
```sh
git clone https://github.com/ronbenbenishti/PDF-downloader.git
```

## How to use ##
```sh
chmod +x pdf-downloader.py
./pdf-downloader
```
