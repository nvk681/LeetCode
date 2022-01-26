class Solution:
    def findReplaceString(self, s, indices, sources, targets) -> str:
        s = list(s)
        new_list = []
        start = 0
        n = len(indices)
        for i in range(n):
            for j in range(0, n-i-1):
                if indices[j] > indices[j + 1] :
                    indices[j], indices[j + 1] = indices[j + 1], indices[j]
                    sources[j], sources[j + 1] = sources[j + 1], sources[j]
                    targets[j], targets[j + 1] = targets[j + 1], targets[j]
        for index in range(len(indices)):
            replace = False 
            if s[indices[index]:indices[index]+len(sources[index])] == list(sources[index]):
                replace = True
            if replace:
                new_list = new_list + s[start:indices[index]]+[targets[index]]#+s[indices[index]+len(sources[index]):]
                start = indices[index]+len(sources[index])
        if start < len(s):
            new_list = new_list +s[start:]
        string = ""
        return string.join(new_list)

# s = Solution()
# print(s.findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]))
# print(s.findReplaceString("abcd", [0, 2], ["ab","ec"], ["eee","ffff"]))
# print(s.findReplaceString("abcd", [0, 2], ["ab","ec"], ["eee","ffff"]))
# print(s.findReplaceString("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"]))