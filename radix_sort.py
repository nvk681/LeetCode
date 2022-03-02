# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.

def sort_based_on_base(arr, base):
    n = len(arr)
    count, result = [0]*10, [0]*n
    for i in arr:
        div = i//base
        count[div%10] += 1
    for index in range(1,10):
        count[index] += count[index-1] 
    index = n-1
    while index > 0:
    # for index in range(n):
        result[count[(arr[index]//base)%10]-1] = arr[index]
        count[(arr[index]//base)%10] -= 1
        index -= 1
    # arr = result
    return result

def sort_by_redix(arr):
    max_digit = max(arr)
    base = 1
    while max_digit/base > 1:
        arr = sort_based_on_base(arr, base)
        base *= 10
    return arr



arr = [170, 45, 75, 90, 802, 24, 2, 66]

arr = sort_by_redix(arr)

print(arr)