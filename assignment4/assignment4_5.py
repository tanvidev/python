arr = list();

num = input("Enter a number - ");

for i in range(num):
    no = input("Enter a no - ");
    arr.append(no);

print "The entered number of list is - ", arr;

def checkPrime(num):
    flag = 0;
    m = num / 2;
    number = range(2, m+1);

    if(num == 0 or num == 1):
        return False;
    else:
        for i in number:
            if(num % i == 0):
                return False;
                flag = 1;
                break;

    if(flag == 0):
        return True;

arr1 = list(filter(lambda no: checkPrime(no), arr));
print "The filtered list is - ", arr1 ;

arr2 = list(map(lambda no: no*2, arr1));
print "The mapped list is - ", arr2 ;

max = reduce(lambda a,b: a if(a>b)else b, arr2);
print "The maximum of all is - ", max;
