import marvellousNum

arr = list();
arrPrime = list();
count = 0;
addPrime = 0;

num = input("Enter no of elements - ");

for i in range(num):
    no = input("Enter number - ");
    arr.append(int(no));
    prime = marvellousNum.checkPrime(no);
    if prime:
        arrPrime.append(no);
        addPrime = addPrime + no;

print("Entered elements are - ", arr);

print("Entered prime elements are - ", arrPrime);

print("The addition of all prime numbers is - ", addPrime);