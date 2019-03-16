def patternStar(num):
    r = range(1, num+1)
    for i in r:
        print("* " * num);


num = input("Enter a number - ");
patternStar(num);
