import threading


def getEvenSum(arr):
    sum = 0;

    for i in range(len(arr)):
        if(i%2 == 0):
            sum = sum + arr[i];

    print sum;


def getOddSum(arr):
    sum = 0;

    for i in range(len(arr)):
        if (i%2 != 0):
            sum = sum + arr[i];

    print sum;


if __name__ == "__main__":
    arr = list(range(1, 50));

    thread1 = threading.Thread(target=getEvenSum, args=(arr,));

    thread2 = threading.Thread(target=getOddSum, args=(arr,));

    thread1.start();
    thread2.start();

    thread1.join();
    thread2.join();



