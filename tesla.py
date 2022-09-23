import math

def check_if_winner(matrix, flag):
    result = True
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == flag:
                result = True
            else:
                return False
    return result

def check_winner(s):
    lenght_of_string = len(s)
    n = math.sqrt(lenght_of_string)
    matrix = []
    pointer = 0
    for _ in range(n):
        temp = []
        for _ in range(n):
            temp.append(s[pointer])
            pointer += 1
        matrix.append(temp)
    O = check_if_winner(matrix, "O")
    if O:
        return "O"
    X = check_if_winner(matrix, "X")
    if X:
        return "X"
    return None


check_winner("");