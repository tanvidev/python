def pattern(num):
    while (num > 0):
        print("* " * num);
        num = num - 1;


num = input("Enter a number - ");
pattern(num);
