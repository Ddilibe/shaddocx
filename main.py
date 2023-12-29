#!/bin/env python3
from utils.urlutils import url_valid
from utils.traverse import VideoClass

def main(url):
    print(url)
    print("[+] - URL Is Valid" if url_valid(url) else "[-] - URL Is Invalid")
    vid = VideoClass(url, filename="blink-182 whats my age")
    

if __name__ == "__main__":
    # there should be option of changing where the videos are downloaded
    url = input("Enter the URL: ")
    main(url)