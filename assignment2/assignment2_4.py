def getFactors(num):
    number = range(1, num+1);
    sum =0;

    for i in number:
        if(num % i == 0):
            print(i);
            sum = sum + i;

    print "Addition of factors is - ", sum;


num = input("Enter a number - ");
getFactors(num);