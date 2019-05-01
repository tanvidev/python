import psutil;
from sys import *;



def processDisplay(processName):

    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                pinfo = proc.as_dict(attrs=['pid', 'name', 'username']);
                processI = pinfo;
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass;

    return processI;



def main():

    print ("Application Name -", argv[0]);

    print("Process Monitor");

    processInfo = processDisplay(argv[1]);

    print (processInfo);


if __name__ == "__main__":
    main();


