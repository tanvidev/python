def add(num1, num2):
    ans = num1 + num2;
    print "Addition is - ", ans;


def sub(num1, num2):
    if(num1 > num2):
        ans = num1 - num2;
    else:
        ans = num2 - num1;
    print "Subtraction is - ", ans;


def mult(num1, num2):
    ans = num1 * num2;
    print "Multiplication is - ", ans;


def div(num1, num2):
    if (num1 > num2):
        ans = num1 / num2;
    else:
        ans = num2 / num1;
    print "Division is - ", ans;

