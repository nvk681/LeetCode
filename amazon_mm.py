from collections import Counter

def get_pairs(processed_inputs):
    
    input = []
    for current_string in processed_inputs:
        previous = ord(current_string[0])
        value = []
        for index in range(1, len(current_string)):
            current = ord(current_string[index])
            value.append(str(current - previous))
            previous = current
        input.append("".join(value))

    pairs = 0
    item_repetation_count = dict(Counter(input))
    for value in item_repetation_count.values():
        if value > 1:
            pairs += (value-1)
    return pairs

print(get_pairs(["corn", "horn", "dpso", "eqtp","corn"]))
print(get_pairs(["cbu", "bat", "cbu"]))