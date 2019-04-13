import threading

print "Assignment - 8, program - 2";

def printEvenFactotrs(num):
    print "\n Even factors sum - ";
    sum = 0
    for i in range(1, num):
        if(num%i==0):
            if(i%2==0):
                sum += i;
    print(sum);

def printOddFactotrs(num):
    print "\n Odd factors sum - ";
    sum = 0
    for i in range(1, num):
        if(num%i==0):
            if(i%2!=0):
                sum += i;
    print(sum);

if __name__ == "__main__":

    number = 48;

    thread1 = threading.Thread(target=printEvenFactotrs, args=(number,));

    thread2 = threading.Thread(target=printOddFactotrs, args=(number,));

    thread1.start();
    thread2.start();

    thread1.join();
    thread2.join();

    print "Exit from main";