# BROKEN LINKS FINDER
# Author: Michele Dalle Rive

import requests
import os
from bs4 import BeautifulSoup
from glob import glob
from urllib.parse import urlparse

def is_absolute(url):
    return bool(urlparse(url).netloc)

def find_broken_links(path, html):
    invalid_urls = []
    soup = BeautifulSoup(html,features="html.parser")
    for link in soup.find_all("a"):
        url = link.get("href")
        if url=="#": continue
        if is_absolute(url):
            try:
                resp = requests.get(url)
                code = resp.status_code
                if code!=200:
                    invalid_urls.append(url)
            except requests.exceptions.RequestException as e:
                invalid_urls.append(url)
        else:
            base_url = soup.find("base").get("href")
            joined_path = os.path.join(os.path.dirname(path), base_url, url)
            if not os.path.exists(joined_path):
                invalid_urls.append(url)

    urls_with_line = {}
    for i,line in enumerate(str(soup).split("\n")):
        for invalid in invalid_urls:
            if invalid in line:
                urls_with_line[invalid]=i+1
    
    return urls_with_line

files = glob("**/*.html", recursive=True)
for f in files:
    print(f)
    content = open(f, encoding="utf8")
    broken_links = find_broken_links(f, content)
    if len(broken_links)==0:
        print("- No broken link found")
    for link in broken_links.keys():
        print("-", "Line", broken_links[link], "->", link, "is invalid")
    print()