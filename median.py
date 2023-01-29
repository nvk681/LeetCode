def findMedianSortedArrays(nums1, nums2) -> float:
        size = len(nums1)+len(nums2)
        if size%2 == 0:
            index = [size//2-1, size//2]
        else:
            index = [size//2]
        print(index)
        result = []
        i1, i2 = 0, 0
        for i in range(size):
            if i1 >= len(nums1):
                value = nums2[i2]
                i2 += 1
            elif i2 >= len(nums2):
                value = nums1[i1]
                i1 += 1
            elif nums1[i1] < nums2[i2]:
                value = nums1[i1]
                i1 += 1
            else:
                value = nums2[i2]
                i2 += 1
            if i in index:
                result.append(value)
            if i > max(index):
                break;
        return sum(result)
findMedianSortedArrays([1,3],[2])