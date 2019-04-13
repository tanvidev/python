class Circle:
    pie = 3.14;

    def __init__(self):
        self.radius = 0.0;
        self.area = 0.0;
        self.circumference = 0.0;

    def accept(self):
        self.radius = input("Enter radius - ");

    def calculateArea(self):
        self.area = 3.14 * self.radius * self.radius;

    def calculateCircumference(self):
        self.circumference = 2 * 3.14 * self.radius;

    def display(self):
        print "The radius is - ", self.radius;
        print "The area is - ", self.area;
        print "The circumference is - ", self.circumference;

obj1 = Circle();

obj1.accept();
obj1.calculateArea();
obj1.calculateCircumference();
obj1.display();

