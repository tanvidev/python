import os
import requests
from sys import *
from urllib.parse import urlparse

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

def downloadFile(URL):
    allowed = is_downloadable(URL);

    if allowed:
        try:
            res = requests.get(URL, allow_redirects = True);

            filename = get_filename_from_cd(URL);
            fd = open(filename, "wb");

            for buffer in res.iter_content(1024):
                fd.write(buffer);

            fd.close();
            return True;
        except Exception as E:
            return False;

    else:
        return False;



def main():
    print("Application Name: ", argv[0]);

    if(len(argv) == 2):
        if(argv[1] == '-h' or argv[1] == '-H'):
            print("This script is used to download file");
            exit();

        if (argv[1] == '-u' or argv[1] == '-U'):
            print("This script is used to download file");
            exit();

    url = "https://www.google.com/favicon.ico";

    result = downloadFile(url);

    if(result == True):
        print("File downloaded successfully");
    else:
        print("Failed to download");


if __name__ == "__main__":
    main();
