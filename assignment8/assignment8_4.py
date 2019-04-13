import threading;


def getSmalls(arr):
    sum = 0;
    for i in range(len(arr)):
        if arr[i].islower():
            sum += 1;

    print "\n ID of Thread1 is - ", threading.current_thread().ident;
    print "\n Name of Thread1 is - ",threading.current_thread().getName();
    print "\n Small letters in string are - ", sum;


def getCapitals(arr):
    sum = 0;
    for i in range(len(arr)):
        if arr[i].isupper():
            sum += 1;

    print "\n Id of Thread2 is - ", threading.current_thread().ident;
    print "\n Name of Thread2 is - ", threading.current_thread().getName();
    print "\n Capital letters in string are - ", sum;


def getNumbers(arr):
    sum=0;
    for i in range(len(arr)):
        if arr[i].isdigit():
            sum += 1;

    print "\n Id of Thread3 is - ", threading.current_thread().ident;
    print "\n Name of Thread3 is - ", threading.current_thread().getName();
    print "\n No of digits in string are - ", sum;

if __name__ == "__main__":

    arr = "Marvellous Infosystem - Python 3 atch No. 1";

    thread1 = threading.Thread(target=getSmalls, args=(arr, ));

    thread2 = threading.Thread(target=getCapitals, args=(arr, ));

    thread3 = threading.Thread(target=getNumbers, args=(arr, ));

    thread1.start();
    thread2.start();
    thread3.start();

    thread1.join();
    thread2.join();
    thread3.join();

