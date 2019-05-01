import os;
import bs4;
import requests;
from sys import *;
from urllib.request import urlopen;


def amazonUrlScrapper(url):

    connection = urlopen(url);

    raw_html = connection.read();

    connection.close();

    page_soup = bs4.BeautifulSoup(raw_html,"html.parser");

    container = page_soup.findAll("a", {"class":"a-link-normal a-text-normal"});

    return container;

def main():
    print("Application Name: ", argv[0]);

    if(len(argv) == 2):
        if(argv[1] == '-h' or argv[1] == '-H'):
            print("This script is used to fetch urls from wikipedia page");
            exit();

        if (argv[1] == '-u' or argv[1] == '-U'):
            print("This script is used to fetch urls from wikipedia page");
            exit();

    url = "https://www.amazon.in/s?k=macbook&ref=nb_sb_noss";

    links = amazonUrlScrapper(url);

    print("URLs are - ");
    for link in links:
            print("\n", link['href'])



if __name__ == "__main__":
    main();