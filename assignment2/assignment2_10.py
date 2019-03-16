def addNum(number):
    count = 0;
    num = 0;

    while(number>0):
        num = number%10;
        count = count + num;
        number = number/10;

    print "Addition is - ", count;


num = input("Enter a number - ");
addNum(num);
