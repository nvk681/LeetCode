class Solution:
    def findOriginalArray(self, changed):
        if len(changed)%2 != 0: return []
        changed.sort()
        original = []
        count = {}
        
        for i in changed:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for i in changed:
            if count[i] <= 0: continue
            count[i] -= 1
            half = int(i/2)
            
            if i%2 == 0 and half in count and count[half] > 0:
                original.append(half)
                count[half] -= 1
                continue
                
            double = i*2
            
            if double in count and count[double] > 0:
                count[double] -= 1
                original.append(i)
                continue
            return []
        
        return original
s = Solution()
print(s.findOriginalArray([4,8,2,16,1,8]))