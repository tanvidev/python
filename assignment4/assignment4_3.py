arr = list();

num = input("Enter a number - ");

for i in range(num):
    no = input("Enter no - ");
    arr.append(no);

print("Entered list of numbers is - ",arr);

arr1 = list(filter(lambda no: (no>=70 and no<=90),arr));\
print "Filtered list is - ",arr1 ;

arr2 = list(map(lambda no: no + 10, arr1));
print "Mapped list is - ",arr2 ;

multi = reduce(lambda a,b: a*b, arr2);

print "The multiplication of all numbers is - ", multi ;

