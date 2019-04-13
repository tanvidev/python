import threading

print("Assignment8_1")

def printEven():
    print("Even number - ")
    for i in range(21):
        if(i % 2 == 0):
            print(i)

def printOdd():
    print("Odd number - ")
    for i in range(21):
        if(i % 2 != 0):
            print(i)

if __name__ == "__main__":

    thread1 = threading.Thread(target=printEven, args=());

    thread2 = threading.Thread(target=printOdd, args=());

    thread1.start();
    thread2.start();

    thread1.join();
    thread2.join();





