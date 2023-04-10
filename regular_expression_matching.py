from functools import lru_cache


def isMatch(s: str, p: str):
        @lru_cache
        def check(i, j):
            if i < len(s) and j == len(p):
                return False
            if i == len(s) and j == len(p):
                return True
            if p[j] == ".":
                if p[j] == s[i]:
                    return check(i+1, j+1)
                else:
                    return False
            value = False
            if p[j] == ".":
                value = value or check(i+1, j+1)
            if j+1 < len(p) and p[j+1] == "*":
                if s[i] == p[j]:
                    value = value or check(i+1, j+2)
                    value = value or check(i+1, j)
                    return value
                if p[j] == ".":
                    return check(i+1, j+2)
            if s[i] == p[j]:
                return check(i+1, j+1)

        return check(0, 0)

a = isMatch("aa", "a*")
print(a==True)

a = isMatch("aab", "c*a*b")
print(a==True)

a = isMatch("aa", "a")
print(a==False)

a = isMatch("aa", "a*")
print(a==True)

a = isMatch("ab", ".*")
print(a==True)