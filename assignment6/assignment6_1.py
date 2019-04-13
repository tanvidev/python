class Demo:

    value = 0;

    def __init__(self,no1,no2):
        self.no1 = no1;
        self.no2 = no2;

    def fun(self):
        print "Inside fun";
        print "The value of no1 is - ", self.no1;
        print "The value of no2 is - ", self.no2;

    def gun(self):
        print "Inside gun";
        print "The value of no1 is - ", self.no1;
        print "The value of no2 is - ", self.no2;


obj1 = Demo(11, 21);
obj2 = Demo(51, 101);

obj1.fun();
obj1.gun();

obj2.fun();
obj2.gun();