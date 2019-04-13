s = str(input("Enter a string - "));

def findAvg(s):
    sum = 0;
    avg = 0;

    for i in s:
        sum = sum + ord(i);

    avg = sum/len(s);
    return avg;

print "Average is - ", findAvg(s);
