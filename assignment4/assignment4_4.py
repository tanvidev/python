arr = list();

num = input("Enter a number - ");

for i in range(num):
    no = input("Enter a no - ");
    arr.append(no);

print "The entered number of list is - ", arr;

arr1 = list(filter(lambda no: (no%2==0), arr));
print "The filtered list is - ", arr1 ;

arr2 = list(map(lambda no: no*no, arr1));
print "The mapped list is - ", arr2 ;

sum = reduce(lambda a,b: a+b, arr2);
print "The addition of all is - ", sum;