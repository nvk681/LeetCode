class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_lenght = len(nums1)+len(nums2)
        new_list = []
        max_lenght = 0

        if total_lenght%2 == 0:
            m2 = total_lenght//2
            m1 = m2-1
            max_lenght = m2
        else:
            m1 = (total_lenght//2)
            max_lenght = m1

        while len(new_list) <= max_lenght and len(nums1) and len(nums2):
            if nums1[0] > nums2[0]:
                new_list.append(nums2.pop(0))
            else:
                new_list.append(nums1.pop(0))
        if len(new_list) <= max_lenght:
            if len(nums1) > 0:
                new_list = new_list + nums1
            else: 
                new_list = new_list + nums2
        if total_lenght%2 == 0:
            return (new_list[m1]+new_list[m2])/2
        else:
            return new_list[m1]