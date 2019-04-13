from os import path;


isExist = path.exists("Demo.txt");

if isExist:
    print "{} File exist.".format("Demo.txt");
else:
    print "File does not exist.".format("Demo.txt");