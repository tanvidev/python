def countNumLength(num):
    count = 0;
    while(num>0):
        num = num/10;
        count = count + 1;

    print "The length is - ", count;


num = input("Enter a number - ");
countNumLength(num);
