from sys import *;
import os;
import shutil;


def copyFiles(dir1, dir2, extension):

    flag = os.path.isabs(dir1);

    if(flag==False):
        path1 = os.path.abspath(dir1);
        path2 = os.path.abspath(dir2);

    exist = os.path.isdir(path1);

    if(exist):
        print "Path1 - ", path1;
        print "Path2 - ", path2;
        for file in os.listdir(path1):
            if file.endswith(extension):
                shutil.copyfile(path1, path2);
    else:
        print "Error: Invalid path.";


def main():
    print "Application name - ", argv[0];

    if(argv[1] == '-h' or argv[1] == 'H'):
        print "This script is used to copy all files with given extension from 1st directory to second directory mentioned.";

    if(argv[1] == '-u' or argv[1] == '-U'):
        print "Usage: Copy all files.";

    if(len(argv) != 4):
        print "Error: Invalid no of arguments";

    try:
        copyFiles(argv[1], argv[2], argv[3]);
    except Exception as e:
        print "Error : ",e;

if __name__ == "__main__":
    main();