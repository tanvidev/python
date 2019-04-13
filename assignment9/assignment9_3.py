import sys;


file = sys.argv[1];

fd = open(file,"r+");

with open("Demo.txt", "r")as f:
    with open(file, "r+") as f1:
        for line in f:
            f1.write(line);

print(fd.read());

fd.close();

