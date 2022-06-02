def reverseWords(s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()# = s[::-1]
        slow, fast = 0,0
        while fast < len(s):
            while fast < len(s) and s[fast] != " ":
                fast += 1
            temp_f = fast
            fast -= 1
            while fast> slow and fast > 0 and slow < len(s):
                s[slow], s[fast] = s[fast], s[slow]
                slow += 1
                fast -= 1
            slow, fast = temp_f+1, temp_f+1
        print(s)

reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])
        