def calculate_strenght(password):
    check = ['a', 'e', 'i', 'o', 'u']
    score = 0
    vowels, cons = 0, 0
    for i in password:
        if i in check:
            vowels += 1
        else:
            cons += 1
        if vowels > 0 and cons > 0:
            score += 1
            vowels, cons = 0, 0
    return score