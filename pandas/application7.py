import os
import fnmatch
from sys import *
import xlsxwriter


def excelCreate(name):

    workbook = xlsxwriter.Workbook(name);

    worksheet = workbook.add_worksheet();

    worksheet.write('A1', 'Name');
    worksheet.write('B1', 'College');
    worksheet.write('C1', 'Mail ID');
    worksheet.write('D1', 'Mobile');

    workbook.close();

def main():
    print("Application Name: ", argv[0]);

    if(len(argv) != 2):
        print("Error: Invalid no of arguments");
        exit();

    if (argv[1] == '-h' or argv[1] == '-H'):
        print("This script is used to excel file and write data into it.");
        exit();

    if (argv[1] == '-u' or argv[1] == '-U'):
        print("Usage: ApplicationName Name_of_file.");
        exit();

    try:
       excelCreate(argv[1]);

    except Exception as E:
        print("Error: Invalid input", E);

if __name__ == "__main__":
    main();