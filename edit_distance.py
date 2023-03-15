from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache
        def get_distance(i1, i2):
            if i1 == len(word1) and i2 < len(word2):
                return len(word2) - i2
            if i1 < len(word1) and i2 == len(word2):
                return len(word1) - i1
            if i1 == len(word1) and i2 == len(word2):
                return 0
            if word1[i1] == word2[i2]:
                return get_distance(i1+1, i2+1)

            min_distance = len(word1)+len(word2)
            min_distance = min(min_distance, get_distance(i1+1,i2)+1)
            min_distance = min(min_distance, get_distance(i1+1, i2+1)+1)
            min_distance = min(min_distance, get_distance(i1, i2+1)+1)

            return min_distance
        return get_distance(0, 0)