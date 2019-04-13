num1 = input("Enter number 1 - ");
num2 = input("Enter number 2 - ");

fp = lambda no1, no2: no1 + no2;

addition = fp(num1,num2);

print "The addition of {} and {} is".format(num1, num2),addition ;

