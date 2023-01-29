
from collections import Counter

def get_pairs(arr):
    # O(N)
    count = Counter(arr)
    pair = 0
    for current_string in arr:
        value = ""
        for current_character in current_string:
            value += chr(ord(current_character) + 1) if current_character != 'z' else 'a'
        if value in count:
            pair += count[value]

    return pair

print(get_pairs(["corn", "horn", "dpso", "eqtp","corn"]))
print(get_pairs(["cbu", "bat", "cbu"]))
# print(rotateString("corn", "dpso"))