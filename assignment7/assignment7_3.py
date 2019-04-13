class Arithmetic:

    def __init__(self, number):
        self.number = number;

    def checkPrime(self, num):
        flag = 0;
        m = num / 2;
        number = range(2, m + 1);

        if (num == 0 or num == 1):
            return False;
        else:
            for i in number:
                if (num % i == 0):
                    return False;
                    flag = 1;
                    break;

        if (flag == 0):
            return True;

    def checkPerfect(self, num):
        sum = 0;
        for i in range(1, num-1):
            if(num%i == 0):
                sum += i;
        if(num == sum):
            return True;
        else:
            return False;

    def getFactors(self, num):
        factors = list();
        for i in range(1, num+1):
            if(num % i == 0):
                factors.append(i);

        return factors;

    def sumOfFactors(self, num):
        sum = 0;
        factors = self.getFactors(num);
        for i in range(len(factors)):
            sum += factors[i];

        return sum;

    def display(self):
        if(self.checkPrime(self.number)== True):
            print "\n {} is a prime number.".format(self.number);
        else:
            print "\n {} is a not prime number.".format(self.number);

        if (self.checkPerfect(self.number) == True):
            print "\n {} is a perfect number.".format(self.number);
        else:
            print "\n {} is a not perfect number.".format(self.number);

        print "\n Factors of {} are - ".format(self.number), self.getFactors(self.number);

        print "\n Sum of Factors of {} is - ".format(self.number), self.sumOfFactors(self.number);


obj1 = Arithmetic(50);
obj1.display();

obj2 = Arithmetic(17);
obj2.display();

obj3 = Arithmetic(6);
obj3.display();







