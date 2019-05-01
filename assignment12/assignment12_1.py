import psutil;
from sys import *;


def processDisplay():
    listProcess=[];

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username']);
            vms = proc.memory_info().vms / (1024 * 1024);
            pinfo['vms'] = vms;
            listProcess.append(pinfo);
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass;

    return listProcess;

def main():

    print ("Application Name -", argv[0]);

    print("Process Monitor");

    listProcess = processDisplay();

    for element in listProcess:
        print(element);


if __name__ == "__main__":
    main();