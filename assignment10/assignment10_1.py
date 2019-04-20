from sys import *;
import os;

def getFiles(path, extension):
    flag = os.path.isabs(path);

    if(flag == False):
        path = os.path.abspath(path);

    exist = os.path.isdir(path);

    if(exist):
        count = 0;
        for file in os.listdir(path):
            if file.endswith(extension):
                print(os.path.join("path", file));
                count += 1;
        if(count == 0):
            print "No file found with extension ",extension;
    else:
        print "Error: Invalid path";


def main():
    print "Application name: ", argv[0];

    if(len(argv) != 3):
        print "Invalid no of arguments.";

    if(argv[1] == '-h' or argv[1] == '-H'):
        print "This script is used to display all files having extension given.";

    if (argv[1] == '-u' or argv[1] == '-U'):
        print "Usage: All files with same extension.";

    try:
        getFiles(argv[1], argv[2]);
    except Exception as e:
        print "Error: ",e;

if __name__ == "__main__":
    main();