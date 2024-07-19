#!/usr/bin/env python3
#
# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
# Longest Increasing Subsequence
# Zastosowanie do permutation graphs (iset).

def find_maximum_iset(perm):
    n = len(perm)
    lis = [1] * n   # dlugosc najlepszej sekwencji o koncu w i
    prev = [None] * n
    for i in range(1, n):
        for j in range(i):
            if perm[j] < perm[i] and lis[i] < lis[j]+1:
                lis[i] = lis[j] + 1
                prev[i] = j
    # Koniec najdluzszej sekwencj jest w i_max.
    i_max = max(range(n), key=lambda i: lis[i])
    i = i_max
    seq = [perm[i_max]]
    while prev[i] is not None:
        i = prev[i]
        seq.append(perm[i])
    seq.reverse()   # dla iset kolejnosc liczb nie ma znaczenia
    return seq

if __name__ == "__main__":

    print ( "longest increasing subsequence ..." )
    assert find_maximum_iset([1, 3, 2]) == [1, 3]
    assert find_maximum_iset([15, 27, 14, 38, 63, 55, 46, 65, 85]) == [15, 27, 38, 63, 65, 85]
    assert find_maximum_iset([5, 4, 3, 2, 1]) == [5]

# EOF
