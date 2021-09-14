#count transpose
from itertools import permutations
l = list(permutations(range(1, 4)))
print (l)
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
for permutation in l:
    n = len(permutation)
    print(noOfTranspositions(permutation, n))
 

