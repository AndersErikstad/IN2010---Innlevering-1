def sort(A):
    # Do insertion sort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    for i in range(1, len(A)):
        j = i - 1
        while j>= 0:
            if A[i]<A[j]:
                A.swap(i, j)
                j -= 1
                i = j + 1
            else:
                break

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.
    return A
