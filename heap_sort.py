def heap_sort(A):
    def swap(i, j):
        A[i], A[j] = A[j], A[i]
    def heap(i,limit):
        while True:
            left_child, right_child = i*2+1, i*2+2
            if max(left_child, right_child) < limit:
                if A[i] < max(A[left_child], A[right_child]):
                    if A[left_child] > A[right_child]:
                        swap(i, left_child)
                        i = left_child
                    else:
                        swap(i, right_child)
                        i = right_child
                else:
                    break
            elif left_child < limit:
                if A[left_child] > A[i]:
                    swap(left_child, i)
                    i = left_child
                else:
                    break
            elif right_child < limit:
                if A[right_child] > A[i]:
                    swap(right_child, i)
                    i = right_child
                else:
                    break
            else: break
    for index in range((len(A)-2)//2, -1, -1):
        heap(index, len(A))
    for end in range(len(A)-1, 0, -1):
        swap(0, end)
        heap(0, end)
    return A

print(heap_sort([1,2,3,4]))
print(heap_sort([4,3,2,1]))
print(heap_sort([12,43,12,54,23,64,67,86,101]))