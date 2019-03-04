#! /usr/local/bin/python3

import random

def main():
    #numArray = read_array_from_file(sys.argv[1])

    numArray = generate_array(11)
    print("The unsorted array: ")
    print(numArray)

    arrayInversions = get_inv_count(numArray, len(numArray))
    print("Number of inversions in input array: " + str(arrayInversions))

    mergeSortArray = merge_sort(numArray)
    print(mergeSortArray)

    median = get_lower_median(mergeSortArray)
    print("Lower median is after merge: " + str(median))

    if len(numArray) % 2 == 0:
        print("Lower median is after selection: " + str(selection(numArray, 0, len(numArray) - 1, int(len(numArray)/2)-1)))
    else:
        print("Lower median is after selection: " + str(selection(numArray, 0, len(numArray) - 1, int(len(numArray)/2))))

def read_array_from_file(filename):
    with open(filename) as f:
        content = [[int(x) for x in line.split()] for line in f]

    numArray = content[0]
    return numArray

def generate_array(n):
    return random.sample(range(0, 20), n)

def merge_sort(A):
    # Base case. A list of zero or one elements is sorted, by definition.
    if len(A) <=1:
        return A

    # Recursive case. Divide A into two arrays, left and right
    left = []
    right = []
    for i in range(len(A)):
        if i < int(len(A)/2):
            left.append(A[i])
        else:
            right.append(A[i])

    # Recursively sort both sublists.
    left = merge_sort(left)
    right = merge_sort(right)

    # Then merge the now-sorted sublists.
    return merge(left, right)

def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    while len(left) > 0:
        result.append(left[0])
        left.pop(0)
    while len(right) > 0:
        result.append(right[0])
        right.pop(0)

    return result


def get_inv_count(arr, n):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1

    return inv_count

def get_lower_median(A):
    if len(A) % 2 == 0:
        return A[int((len(A))/2)-1]
    else:
        return A[int((len(A))/2)]

# def quick_sort(A, p, r):
#     if p < r:
#         q = partition(A, p, r, A[r])
#         quick_sort(A, p, q-1)
#         quick_sort(A, q+1, r)
#
#     return A

def partition(A, lo, hi, p):
    A[lo], A[p] = A[p], A[lo]

    # partition
    i = lo
    for j in range(lo + 1, hi + 1):
        if A[j] < A[lo]:
            i += 1
            A[i], A[j] = A[j], A[i]

    # move pivot to correct location
    A[i], A[lo] = A[lo], A[i]
    return i, A

def selection(A, lo, hi, p):

    # base case, if left eqals right
    if lo == hi:
        return A[lo]

    # choose random pivot
    pivot_index = random.randint(lo, hi)

    i, lst = partition(A, lo, hi, pivot_index)

    # recursively partition one side only
    if p == i:
        return lst[i]
    elif p < i:
        return selection(A, lo, i-1, p)
    else:
        return selection(A, i+1, hi, p)


if __name__ == '__main__':
    main()