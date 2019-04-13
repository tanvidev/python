arr = list();

num = input("Enter number of elements - ");

def findFrequency(arr, element):
    frequency = 0;
    for i in range(len(arr)):
        if arr[i] == element:
            frequency += 1;
    return frequency;


for i in range(num):
    no = input("Enter number - ");
    arr.append(no);

print("Entered numbers in list are - ", arr);

element = input("Enter element to search - ");

print("frequency of {} among list is - ".format(element),findFrequency(arr,element));