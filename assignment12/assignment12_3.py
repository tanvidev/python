import os;
import time;
import psutil;
from sys import *;


def processLog(log_dir):
    listProcess=[];

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir);
        except:
            pass;

    separator = "-" * 80;
    log_path = os.path.join(log_dir, "TanviLog%s.log"%(time.ctime()))
    path = os.path.abspath(log_path);
    print(path)
    f = open(r'path',"w")
    f.write(separator + "\n");
    f.write("Process Logger: "+time.ctime()+"\n");
    f.write(separator + "\n");
    f.write("\n");

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username']);
            vms = proc.memory_info().vms / (1024 * 1024);
            pinfo['vms'] = vms;
            listProcess.append(pinfo);
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass;

    for element in listProcess:
        f.write("%s\n"% element);

    print("Log file is successfully generated at location %s"%(log_path));


def main():

    print ("Application Name -", argv[0]);

    print("Process Monitor");

    processLog(argv[1]);


if __name__ == "__main__":
    main();