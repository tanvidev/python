def checkNum(num):
    if(num % 5 == 0):
        return True;
    else:
        return False;

x = input("Enter a number - ");

ans = checkNum(x);
print(ans);

