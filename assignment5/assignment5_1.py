s = str(input("Enter a string - "));
print "Entered string is - ",s;
s1 = '';

for c in s:
    s1 = c + s1;

print "Reverse of a {} is - ".format(s),s1;