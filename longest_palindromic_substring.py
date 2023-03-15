from functools import lru_cache


def longestPalindrome(s):
        global long_lenght
        long_lenght = 0
        global index, end
        index, end = None, None
        def check_if_palin(i, e):
            temp = s[i:e+1]
            return temp[::-1] == temp
        @lru_cache
        def check_string(i,e):
            if i >= e:
                return None
            if s[i] == s[e]:
                if check_if_palin(i, e):
                    global long_lenght
                    if long_lenght < e-i+1:
                        global index, end
                        index, end = i, e
                        long_lenght = e-i+1
            check_string(i+1, e)
            check_string(i, e-1)
        
        check_string(0, len(s)-1)
        if index is None:
            return s[0]
        else:
            return s[index:end+1]


a = longestPalindrome("babad")
print(a)