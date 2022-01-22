from functools import lru_cache

def wordBreak(s, wordDict) -> bool:
    @lru_cache(None)
    def check(i):
        if i < 0:
            return True
        for word in wordDict:
            if (i >= len(word)-1) and check(i - len(word)):
                if s[i - len(word) + 1 : i+1] == word:
                    return True
        return False
    
    return check(len(s)-1)

print(wordBreak("leetcode", ["leet","code"]))
print(wordBreak("applepenapple", ["apple","pen"]))
print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))