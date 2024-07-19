#!/usr/bin/env python3
#
# https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
# Longest Increasing Subsequence Size (N log N)
# Zastosowanie do permutation graphs (iset).

# Python program to find length of longest 
# increasing subsequence in O(n Log n) time 

# Binary search (note boundaries in the caller) 
# A[] is ceilIndex in the caller

def CeilIndex(A, left, right, key):
    while (left + 1 < right):   # dopoki jest odstep
        m = (left + right) // 2
        if key <= A[m]:
            right = m
        else:   # A[m] < key
            left = m
    #print ( "CeilIndex {}".format(right) )
    return right
    # zawsze A[left] < key <= A[right], chyba dlatego CeilIndex

def LISLength(A):
    size = len(A)
    # Add boundary case, when array size is one 
    tailTable = [0 for i in range(size)]
    length = 0   # always points empty slot (nowe puste miejsce)
    tailTable[0] = A[0]
    length = 1   # tez aktalna dlugosc najdluzszej sekwencji
    for i in range(1, size):
        #print ( "i {} A[i] {}".format(i, A[i]) )
        if A[i] < tailTable[0]:
            # new smallest value
            tailTable[0] = A[i]
        elif A[i] > tailTable[length-1]:
            # A[i] wants to extend largest subsequence 
            tailTable[length] = A[i] 
            length += 1
        else:
            # A[i] wants to be current end candidate of an existing 
            # subsequence. It will replace ceil value in tailTable 
            #tailTable[CeilIndex(tailTable, -1, length-1, A[i])] = A[i] 
            tailTable[CeilIndex(tailTable, 0, length-1, A[i])] = A[i] 
    #print (tailTable)
    return length

if __name__ == "__main__":

    # Driver program to test above function 

    A = [ 2, 5, 3, 7, 11, 8, 10, 13, 6 ]
    print("Length of Longest Increasing Subsequence") 
    print (A, LISLength(A))
    A = [2,4,6]
    print (A, LISLength(A))
    A = [1,5,4,6]
    print (A, LISLength(A))

# EOF
