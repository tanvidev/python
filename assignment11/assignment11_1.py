from sys import *;
import os;
import hashlib;


def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb');
    hasher = hashlib.md5();
    buf = afile.read(blocksize);

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close();

    return hasher.hexdigest();

def displayChecksum(path):
    flag = os.path.isabs(path);

    if (flag == False):
        path = os.path.abspath(path);

    exist = os.path.isdir(path);

    if (exist):
        for dirName, subdirs, fileList in os.walk(path):
            print "\n Current folder is - ", dirName;
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path);
                print(path);
                print(file_hash);
                print('');
    else:
        print "Error: Invalid Path."


def main():
    print "Application name: ", argv[0];

    if(len(argv) != 2):
        print "Invalid no of arguments.";

    if(argv[1] == '-h' or argv[1] == '-H'):
        print "This script is used to traverse specific directory and display checksum of all files.";
        exit()

    if (argv[1] == '-u' or argv[1] == '-U'):
        print "Usage: ApplicationName absolute_path_of_directory extension.";
        exit()

    try:
        arr = displayChecksum(argv[1]);
    except ValueError:
        print("Error: Invalid datatype of input");
    except Exception as e:
        print "Error: ",e;

if __name__ == "__main__":
    main();