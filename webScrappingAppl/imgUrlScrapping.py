import os;
import bs4;
import requests;
from sys import *;
from urllib.request import urlopen


def imageUrlScrapper(url):

    connection = urlopen(url);

    raw_html = connection.read();

    connection.close();

    page_soup = bs4.BeautifulSoup(raw_html,"html.parser");

    container = page_soup.findAll("div", {"class":"item-container"});

    return container;


def main():
    print("Application Name: ", argv[0]);

    if(len(argv) == 2):
        if(argv[1] == '-h' or argv[1] == '-H'):
            print("This script is used to fetch urls of images");
            exit();

        if (argv[1] == '-u' or argv[1] == '-U'):
            print("This script is used to fetch urls of images");
            exit();

    try:

        url = "https://www.newegg.com/Video-cards-Video-Devices/Category/ID-38?Tpk=video%20card";

        links = imageUrlScrapper(url);

        print("URLs are - ");
        for link in links:
                print("\n", link.a.img['data-src']);
    except Exception as E:
        print("Error: Invalid input", E)


if __name__ == "__main__":
    main();