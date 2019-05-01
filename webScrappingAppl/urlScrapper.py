import os
import requests
import bs4
from sys import *


def displayLinks(url):
    res = requests.get(url);
    print(type(res));

    soup = bs4.BeautifulSoup(res.text.encode("utf-8"),'lxml');
    print(type(soup));

    links = soup.find_all('a', href = True);
    return links;

def main():
    print("Application Name: ", argv[0]);

    if(len(argv) == 2):
        if(argv[1] == '-h' or argv[1] == '-H'):
            print("This script is used to fetch urls from wikipedia page");
            exit();

        if (argv[1] == '-u' or argv[1] == '-U'):
            print("This script is used to fetch urls from wikipedia page");
            exit();

    url = "https://en.wikipedia.org/wiki/Python_(programming_language)";

    links = displayLinks(url);

    print("Links are - ");
    for link in links:
        if "#" not in link['href']:
            print(link['href'])


if __name__ == "__main__":
    main();