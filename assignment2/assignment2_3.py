def factorial(num):
    fact = 1
    number = range(1, num+1);
    for i in number:
        fact = fact * i;
    print "Factorial is - ", fact;

num = input("Enter a number - ");
factorial(num);
