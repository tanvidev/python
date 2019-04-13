arr = list()
count = 0;

num = input("Enter no of elements - ");

for i in range(num):
    no = input("Enter number - ");

    arr.append(int(no));
    count = count + no;


print("Entered elements are - ", arr);

print("The addition of all numbers is - ", count);