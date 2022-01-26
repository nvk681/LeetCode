class Solution:
    def findOriginalArray(self, changed):
        if len(changed)%2 != 0:
            return []
        changed.sort()
        c = Counter([1,2,3])
        new_one = []
        zero_count = 0
        if changed.count(0)%2 == 1:
            return []
        else: 
            while changed.count(0) > 0:
                zero_count += 1
                changed.remove(0) 
        i = 0
        half_len =  (len(changed)//2)
        while i < half_len:
            if (2*changed[i] not in changed):
                return []
            else:
                new_one.append(changed[i])
                changed.remove(changed[i]*2)
                i += 1
        if zero_count > 0:
            new_one = new_one+([0]*(zero_count//2))
        return new_one

s = Solution()
print(s.findOriginalArray([0,0,0,0]))
# print(s.findOriginalArray([0,1,0,0]))