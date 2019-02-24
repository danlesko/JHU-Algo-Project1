#! /usr/local/bin/python3

import sys
import random
import math

def main():
    numArray = read_array_from_file(sys.argv[1])
    print(numArray)

    generate_array(10)

    arrayInversions = get_inv_count(numArray, len(numArray))
    print("Number of inversions in input array: " + str(arrayInversions))

    mergeSortArray = merge_sort(numArray)
    print(mergeSortArray)

    median = get_lower_median(mergeSortArray)
    print("Lower median is: " + str(median))

    quikArray = quick_sort(numArray, 0, len(numArray)-1)
    print(quikArray)

    if len(numArray) % 2 == 0:
        print(quickselect(numArray, int(len(numArray)/2)-1))
    else:
        print(quickselect(numArray, int(len(numArray)/2)))

def read_array_from_file(filename):
    with open(filename) as f:
        content = [[int(x) for x in line.split()] for line in f]

    numArray = content[0]
    return numArray

def generate_array(n):
    print(random.sample(range(0, 20), n))

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

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r, A[r])
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

    return A

def partition(A, lo, hi, pivot):
    i = lo-1
    for j in range(lo, hi):
        if A[j] <= pivot:
            i = i + 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    tmp = A[i+1]
    A[i+1] = A[hi]
    A[hi] = tmp
    return i+1

def quickselect(items, item_index):

    def select(lst, l, r, index):

        # base case
        if r == l:
            return lst[l]

        # choose random pivot
        pivot_index = random.randint(l, r)

        # move pivot to beginning of list
        lst[l], lst[pivot_index] = lst[pivot_index], lst[l]

        # partition
        i = l
        for j in range(l+1, r+1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        # move pivot to correct location
        lst[i], lst[l] = lst[l], lst[i]

        # recursively partition one side only
        if index == i:
            return lst[i]
        elif index < i:
            return select(lst, l, i-1, index)
        else:
            return select(lst, i+1, r, index)

    if items is None or len(items) < 1:
        return None

    if item_index < 0 or item_index > len(items) - 1:
        raise IndexError()

    return select(items, 0, len(items) - 1, item_index)

if __name__ == '__main__':
    main()