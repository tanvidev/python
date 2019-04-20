from sys import *;
import os;
import shutil;


def copyFiles(dir1, dir2):
    flag = os.path.isabs(dir1);

    if (flag == False):
        path1 = os.path.abspath(dir1);

    exist = os.path.isdir(path1);

    if exist:
        shutil.copytree(path1, dir2);
    else:
        print "Error: Invalid path.";

def main():
    print "Application name:", argv[0];

    if (len(argv) != 3):
        print "Invalid no of arguments.";

    if (argv[1] == '-h' or argv[1] == '-H'):
        print "This script is used to copy all files from 1st directory to second directory mentioned.";

    if (argv[1] == '-u' or argv[1] == '-U'):
        print "Usage: Copy all files.";

    try:
        copyFiles(argv[1], argv[2]);
    except Exception as e:
        print "Error: ", e;

if __name__  == "__main__":
    main();