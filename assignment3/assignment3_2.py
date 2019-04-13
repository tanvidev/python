arr = list();

num = input("Enter number of elements - ");

for i in range(num):
    no = input("Enter number - ");
    arr.append(no);

print("Entered numbers in list are - ", arr);

print("Maximum number among list is - ", max(arr));