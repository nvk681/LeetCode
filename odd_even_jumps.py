def oddEvenJumps(arr):
        def jump(start):
            jump_no = 1
            while start < len(arr):
                if jump_no%2 == 0:
                    start = min_map[start]
                else:
                    start = max_map[start]
                if start == -1:
                    return False
                jump_no += 1
                if start == len(arr) - 1:
                    return True
            return False
        min_map = [-1]*len(arr)
        max_map = [-1]*len(arr)
        for i in range(len(arr)):
            current_min = -float('inf')
            current_max = float('inf')
            for j in range(i+1,len(arr)):
                if j == len(arr):
                    break
                if arr[j] >= arr[i] and arr[j] < current_max :
                    current_max = arr[j]
                    max_map[i] = j
                if arr[j] <= arr[i] and current_min < arr[j]:
                    current_min = arr[j]
                    min_map[i] = j
        count = 0
        for index in range(len(arr)):
            if jump(index):
                count += 1
        return count+1

# print(oddEvenJumps([10,13,12,14,15]))
print(oddEvenJumps([2,3,1,1,4]))
# print(oddEvenJumps([5,1,3,4,2]))