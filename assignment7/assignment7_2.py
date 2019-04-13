class BankAccount:
    ROI = 10.5;

    def __init__(self, name, amount):
        print "\n";
        self.name = name;
        self.amount = amount;

    def display(self):
        print "Name - ", self.name;
        print "Amount - ",self.amount;

    def deposit(self, amountToDeposite):
        self.amount = int(self.amount) + amountToDeposite;
        print "Amount after depositing amount {} - ".format(amountToDeposite), self.amount;

    def withdraw(self, amountToWothdraw):
        self.amount = int(self.amount) - amountToWothdraw;
        print "Amount after withdrawing amount {} - ".format(amountToWothdraw), self.amount;

    def calculateInterest(self):
        interest = self.amount / BankAccount.ROI;
        print "Interest you will get is - ", interest;

obj1 = BankAccount("Tanvi", "50000");
obj1.display();
obj1.deposit(5000);
obj1.withdraw(2000);
obj1.calculateInterest();

obj2 = BankAccount("Suyog", "100000");
obj2.display();
obj2.deposit(5000);
obj2.withdraw(2000);
obj2.calculateInterest();

