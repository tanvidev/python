arr = list();

num = input("Enter number of elements - ");

for i in range(num):
    no = input("Enter number - ");

    arr.append(no);

print("Numbers entered in list are - ", arr);

print("Minimum number in list is - ", min(arr));