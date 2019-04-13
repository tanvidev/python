def checkPrime(num):
    flag = 0;
    m = num / 2;
    number = range(2, m+1);

    if(num == 0 or num == 1):
        return False;
    else:
        for i in number:
            if(num % i == 0):
                return False;
                flag = 1;
                break;

    if(flag == 0):
        return True;
