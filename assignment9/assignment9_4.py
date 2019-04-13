import sys;


file1 = sys.argv[1];
file2 = sys.argv[2];

f1 = open(file1, "r");
f2 = open(file2, "r");

for line1 in f1:
    for line2 in f2:
        if line1 == line2:
             print "Success";
        else:
            print "Failure";


f1.close();
f2.close();