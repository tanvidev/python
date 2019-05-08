from sys import *;
import os;
import hashlib;
import time;



def deleteFiles(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()));

    inct = 0;

    if len(results) > 0:
        for result in results:
            for subresult in result:
                inct += 1;
                if inct >= 2:
                    os.remove(subresult);
            inct = 0;
    else:
        print("No duplicates file found")


def hashfile(path, blocksize = 1024):
    afile = open(path,'rb');
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def findDuplicates(path):
    flag = os.path.isabs(path);

    if flag == False:
        path = os.path.abspath(path);

    exist = os.path.isdir(path);

    dups = {};

    if exist:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is - ", dirName);
            for filen in fileList:
                path = os.path.join(dirName, filen);
                file_hash = hashfile(path);

                if file_hash in dups:
                    dups[file_hash].append(path);
                else:
                    dups[file_hash] = [path];
        return dups;
    else:
        print("Invalid path");

def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()));
    txtFile = open("log.txt", "w");

    if len(results) > 0:
        for result in results:
            for subresult in result:
                txtFile.write(subresult);
                txtFile.write("\n")
        txtFile.close();
    else:
        print("No duplicate files found");


def main():
    print("Application Name: ", argv[0]);

    if(len(argv) != 2):
        print("Error: Invalid no of arguments");
        exit();

    if (argv[1] == '-h' or argv[1] == '-H'):
        print "This script is used to traverse specific directory and display name of duplicate files.";
        exit();

    if (argv[1] == '-u' or argv[1] == '-U'):
        print "Usage: ApplicationName absolute_path_of_directory extension.";
        exit();

    try:
        arr = {};
        startTime = time.time();
        arr = findDuplicates(argv[1]);
        printResults(arr);
        deleteFiles(arr);
        endTime = time.time();

        print("%s secons taken to evaluate "%(endTime - startTime));

    except ValueError:
        print("Error: Invalid datatype of input");

    except Exception as E:
        print("Error: Invalid input", E);

if __name__ == "__main__":
    main();