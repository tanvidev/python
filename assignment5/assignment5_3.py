from itertools import permutations;

def permutation():
    s = str(input("Enter a string - "));

    permList = permutations(s);
    print "Permutations of {} is - ".format(s), ;
    for perm in permList:
        print(''.join(perm));



permutation();