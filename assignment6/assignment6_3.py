class Arithmetic:
    def __init__(self):
        self.value1 = 0;
        self.value2 = 0;

    def accept(self):
        self.value1 = input("Enter number1 - ");
        self.value2 = input("Enter number2 - ");

    def addition(self):
        print "The addition of {} and {} is -".format(self.value1, self
                                                      .value2), self.value1 + self.value2;

    def subtraction(self):
        if self.value1 > self.value2:
            print "The subtraction of {} and {} is -".format(self.value1, self
                                                          .value2), self.value1 - self.value2;
        else:
            print "The subtraction of {} and {} is -".format(self.value2, self
                                                          .value1), self.value2 - self.value1;

    def multiplication(self):
        print "The multiplication of {} and {} is -".format(self.value1, self
                                                             .value2), self.value1 * self.value2;

    def division(self):
        if self.value1 > self.value2:
            print "The division of {} and {} is -".format(self.value1, self
                                                             .value2), self.value1 / self.value2;
        else:
            print "The division of {} and {} is -".format(self.value2, self
                                                             .value1), self.value2 / self.value1;

obj1 = Arithmetic();

obj1.accept();
obj1.addition();
obj1.subtraction();
obj1.multiplication();
obj1.division();
