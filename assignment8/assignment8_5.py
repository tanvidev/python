import threading;

def printNumbers():
    print "Numbers in order - "
    for i in range(1, 51):
        print i;

def printReverseNumbers():
    print "Numbers in reverse - "
    for i in reversed(range(51)):
        print i;

if __name__ == "__main__":

    thread1 = threading.Thread(target=printNumbers, args=());

    thread2 = threading.Thread(target=printReverseNumbers, args=());

    thread1.start();
    thread1.join();

    thread2.start();
    thread2.join();