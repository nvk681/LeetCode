class Solution:
    def numDecodings(self, s: str) -> int:
        hash_map = {}
        character_map = []
        for i in range(ord('a'), ord('z')+1):
            character_map.append(str(i-ord('a')+1))
        # print(character_map)
        def check_and_return(s, i):
            if i in hash_map:
                return hash_map[i]
            if i == len(s):
                return False
            if s[i] == '0':
                return False
            current_count = 0
            if s[i] in character_map and i == len(s)-1:
                return 1
            if s[i] in character_map:
                result = check_and_return(s,i+1)
                if result:
                    current_count +=  (result)
            if i<len(s)-1 and s[i:i+2] in character_map:
                result = check_and_return(s,i+2)
                if result:
                    current_count += (result)
            if s[i:i+2] in character_map and i == len(s)-2:
                current_count += 1
            hash_map[i] = current_count
            return current_count

        result = check_and_return(s, 0)
        result = result if result is not False else 0
        return result

s = Solution()
print(s.numDecodings("12"))
print(s.numDecodings("226"))
print(s.numDecodings("06"))
# print(s.numDecodings("12"))