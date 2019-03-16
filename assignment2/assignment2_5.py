def checkPrime(num):
    flag = 0;
    m = num / 2;
    number = range(2, m+1);

    if(num == 0 or num == 1):
        print num, "is not a prime number";
    else:
        for i in number:
            if(num % i == 0):
                print num, "is not a prime number";
                flag = 1;
                break;

    if(flag == 0):
        print num, "is a prime number";


num = input("Enter a number - ");
checkPrime(num);
