from sys import *
import os

def directoryWatcher(path):
    flag = os.path.isabs(path);

    if(flag == False):
        path = os.path.abspath(path);

    exist = os.path.isdir(path);
    print "path - ", path;
    print "exist - ", exist;

    if(exist):
        for folderName, subFolder, fileName in os.walk(path):
            print "\n Current folder is - ", folderName;
            for subf in subFolder:
                print "\n Sub folder of {} is - ".format(folderName), subf;
            for file in fileName:
                print "\n File inside {} is - ".format(folderName), file;
    else:
        print "Error: Invalid Path."

def main():
    print "Application name: ", argv[0];

    if(len(argv) != 2):
        print "Error: Invalid no of arguments.";
        exit();

    if(argv[1]=='-h' or argv[1]=='-H'):
        print "This script is used to traversed specific directory.";
        exit();

    if(argv[1]=='-u' or argv[1]=='-U'):
        print "Usage: Absolute path of directory."
        exit();

    try:
        directoryWatcher(argv[1]);
    except ValueError:
        print "Error: Invalid datatype of input";
    except Exception:
        print "Error: Invalid input";

if __name__ == "__main__":
    main();