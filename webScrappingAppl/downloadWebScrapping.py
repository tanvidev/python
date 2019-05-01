import os;
import bs4;
import requests;
from sys import *;
from urllib.parse import urlparse;
from urllib.request import urlopen;


def is_downloadable(URL):
    h = requests.head(URL, allow_redirects = True);
    header = h.headers;
    content_type = header.get('content-type');

    if 'text' in content_type.lower():
        return False;

    if 'html' in content_type.lower():
        return False;

    return True;

def get_filename_from_cd(URL):
    a = urlparse(URL);
    return os.path.basename(a.path);

def downloadImg(url):
    url = "http:" + url;

    allowed = is_downloadable(url);

    if allowed:
        try:
            res = requests.get(url, allow_redirects=True);
            res.raise_for_status();
            filename = get_filename_from_cd(url);
            fd = open(filename, "wb");

            for buffer in res.iter_content(1024):
                fd.write(buffer);

            fd.close();
            return True;
        except Exception as E:
            return False;
    else:
        return False;


def imageUrlScrapper(url):
    try:
        connection = urlopen(url);

        raw_html = connection.read();

        connection.close();

        page_soup = bs4.BeautifulSoup(raw_html,"html.parser");

        container = page_soup.findAll("div", {"class":"item-container"});

        for link in container:
            ret = downloadImg( link.a.img['data-src']);
            if ret == False:
                break;

        return ret;
    except Exception:
        return False;


def main():
    print("Application Name: ", argv[0]);

    if(len(argv) == 2):
        if(argv[1] == '-h' or argv[1] == '-H'):
            print("This script is used to fetch urls of images");
            exit();

        if (argv[1] == '-u' or argv[1] == '-U'):
            print("This script is used to fetch urls of images");
            exit();

        url = "https://www.newegg.com/Video-cards-Video-Devices/Category/ID-38?Tpk=video%20card";

        try:
            res = imageUrlScrapper(url);
            if (res == True):
                print("File downloaded successfully");
            else:
                print("Failed to download");
        except Exception as E:
            print("Error: Invalid input", E)


if __name__ == "__main__":
    main();