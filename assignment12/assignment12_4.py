import os;
import time;
import psutil;
import smtplib;
from sys import *;
from email import encoders;
from email.mime.text import MIMEText;
from email.mime.base import MIMEBase;
from email.mime.multipart import MIMEMultipart;
from urllib.request import urlopen;


def is_connected():
    try:
        urlopen('http://216.58.192.142', timeout = 10);
        return True;
    except Exception as err:
        return False;

def sendMail(user_name, password, filename, time):
    try:
        sent_from = user_name;
        to = ['suyog.rajwal123@gmail.com'];

        msg = MIMEMultipart();

        msg['From'] = sent_from;

        msg['To'] = to;

        body = """
        Hello %s,
        Welcome.
        Please find attached document which contains Log of Running process.
        Log file is created at; %s.
        
        This is an auto generated mail.
        
        Thanks & Regards,
        Tanvi Rajwal
        """%(to, time);

        subject = """ Process Log generated at: %s"""%(time);

        msg['Subject'] = subject;

        msg.attach(MIMEText(body,'plain'));

        attachment = open(filename, 'rb');

        p = MIMEBase('application', 'octate-streaam');

        p.set_payload(attachment.read());

        encoders.encode_base_64(p);

        p.add_header("Content-Desposition", "attachment;filename=%s"%filename);

        msg.attach(p);

        server = smtplib.SMTP('smtp.gmail.com', 565);
        server.starttls;
        server.login(sent_from, password);
        text = msg.as_string();
        server.sendmail(sent_from, to, text);
        server.quit();

        print ("Log file sent successfully")

    except Exception as e:
        print ("Unable to send mail", e);


def processLog(log_dir, mail_id):
    listProcess=[];

    gmailId = mail_id;
    gmail_password = "--------------";

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir);
        except:
            pass;

    separator = "-" * 80;
    log_path = os.path.join(log_dir, "TanviLog%s.log"%(time.ctime()))
    print(log_path)
    f = open(r'log_path',"w")
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

    connected = is_connected();

    if connected:
        startTime = time.time();
        sendMail(gmailId, gmail_password, log_path, time.ctime());
        endTime = time.time();
        print("%s time taken to send a mail"%(endTime - startTime));
    else:
        print("There is no internet connection.");



def main():

    print ("Application Name -", argv[0]);

    if(len(argv)!=3):
        print("Invalid no of arguments");

    try:
        processLog(argv[1], argv[2]);

    except Exception as E:
        print("Error - ", E);

    processLog(argv[1], argv[2]);


if __name__ == "__main__":
    main();