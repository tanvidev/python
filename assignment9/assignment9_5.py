import sys;

file = sys.argv[1];
string = sys.argv[2];
count = 0;

fd = open(file, "r");

for line in fd:
    words = line.split();
    for i in words:
        if (i == string):
            count += 1;

print "Frequency of {} in file is - ".format(string),count;

fd.close();