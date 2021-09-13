#count transpose
def permutation_exist(array):
    for a in range(len(array)-2 , -1 , -1):
        print("\"",array[a],"\"")
        if array[a] < array[a + 1]:
            b = len(array) - 1
            while True:
                # print('h')
                if array[b] > array[a]:
                    array[a], array[b] = array[b], array[a]
                    c = len(array) - 1
                    a = a + 1
                    a = len(array) - 1
                    while(a < b):
                        array[a], array[c] = array[c], array[a]
                        a = a + 1
                        c = c - 1
                    return True
                b = b - 1
    return False

def permutation(sequence):
    list_sequence = [int(a) for a in str(sequence)]
    print(list_sequence)
    while(permutation_exist(list_sequence)):
        for j in list_sequence:
            print(j)

dim_seq = 123
print(permutation(dim_seq))


# Python Program to find the number of
# transpositions in a permutation
N = 1000001
 
visited = [0] * N
 
# This array stores which element goes to which position
goesTo = [0] * N
 
# For eg. in { 5, 1, 4, 3, 2 }
# goesTo[1] = 2
# goesTo[2] = 5
# goesTo[3] = 4
# goesTo[4] = 3
# goesTo[5] = 1
 
# This function returns the size of a component cycle
def dfs(i) :
 
    # If it is already visited
    if (visited[i] == 1) :
        return 0
 
    visited[i] = 1
    x = dfs(goesTo[i])
    return (x + 1)
 
# This functio returns the number
# of transpositions in the permutation
def noOfTranspositions(P, n) :
 
    # Initializing visited[] array
    for i in range(1, n + 1) :
        visited[i] = 0
 
    # building the goesTo[] array
    for i in range(n) :
        goesTo[P[i]] = i + 1
 
    transpositions = 0
 
    for i in range(1, n + 1) :
        if (visited[i] == 0) :
            ans = dfs(i)
            transpositions += ans - 1
 
    return transpositions
 
# Driver Code
permutation = [ 1, 3, 4, 2]
n = len(permutation)
 
print(noOfTranspositions(permutation, n))
 

