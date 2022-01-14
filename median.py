def findMedianSortedArrays(nums1, nums2) -> float:
        index1,index2 = 0,0
        total_lenght = len(nums1)+len(nums2)
        median = list()
        answer = list()
        if total_lenght/2 == total_lenght//2:
            median.append(total_lenght//2)
            median.append(total_lenght//2+1)
        else: 
            median.append(total_lenght//2+1)
        while len(answer) != len(median):
            if (index1+index2+1) in median:
                ans = None
                if index1 >= len(nums1) and index2 < len(nums2):
                    ans = nums2[index2]
                    index2 += 1
                if index2 >= len(nums2) and index1 < len(nums1):
                    ans = nums1[index1]
                    index1 += 1
                if ans is None: 
                    if nums1[index1] < nums2[index2]:
                        ans = nums1[index1]
                        index1 += 1
                    else:
                        ans = nums2[index2]
                        index2 += 1
                answer.append(ans)
            else: 
                if index1 < len(nums1) and index2 < len(nums2):
                    if nums1[index1] < nums2[index2]:
                        index1 += 1
                        continue
                    else: 
                        index2 += 1
                        continue
                if index1 >= len(nums1):
                    index2 += 1
                    continue
                if index2 >= len(nums2):
                    index1 += 1
                    continue
        if len(answer) == 1:
            return answer[0]
        else: 
            return sum(answer)/2
findMedianSortedArrays([1,3],[2])