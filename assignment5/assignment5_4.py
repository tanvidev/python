s = str(input("Enter a string - "));

p = input("Enter the position - ");

def strFun(s,p):
    str = s[:p] + s[p+1:];
    return str;

print "Output - ",strFun(s, p);