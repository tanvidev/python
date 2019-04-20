from sys import *;
import os;


def copyFiles(path, ext1, ext2):
    flag = os.path.isabs(path);

    if(flag == False):
        path = os.path.abspath(path);

    exist = os.path.isdir(path);

    if(exist):
        for file in os.listdir(path):
            filename = os.path.join(path, file);
            if not os.path.isfile(filename): continue;
            old = os.path.splitext(file);
            newname = filename.replace(ext1, ext2);
            newFileName = os.rename(filename, newname);
    else:
        print "Error: Invalid path";


def main():
    print "Application name: ", argv[0];

    if (len(argv) != 4):
        print "Invalid no of arguments.";

    if (argv[1] == '-h' or argv[1] == '-H'):
        print "This script is used to rename all files in a directory with given extension.";

    if (argv[1] == '-u' or argv[1] == '-U'):
        print "Usage: Copy all files with same extension.";

    try:
        copyFiles(argv[1], argv[2], argv[3]);
    except Exception as e:
        print "Error: ", e;


if __name__ == "__main__":
    main();