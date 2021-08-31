# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    a=[]
    h=0
    if len(lst)== len(lst[0]):
        for i in range(len(lst)):
            for j in range(len(lst)):
                a.append(lst[i][j])
            break
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j] in a and lst[i][j] in a:
                continue
            else:
                return False
    return True
lst = [[1, 2, 3],
       [3, 1, 2],
       [2, 3, 1]]
assert(isLatinSquare(lst) == True)
 
lst1 = [[1, 2, 3, 4],
        [4, 1, 2, 3],
        [3, 4, 1, 2],
        [2, 3, 4, 1]]
assert(isLatinSquare(lst1) == True)
 
lst2 = [[1, 2, 3, 4],
        [2, 1, 3, 4],
        [3, 4, 2, 1],
        [4, 1, 3, 2]]
assert(isLatinSquare(lst2) == False)
print("All test cases passed...!")

