def calculator(operation, num1, num2):
    if operation == "+":
        return num1+num2
    if operation == "-":
        return num2-num1
    if operation == "/":
        if abs(num2) < abs(num1): return 0
        return int(num2/num1)
    if operation == "*":
        return num1*num2



def evalRPN(tokens) -> int:
    stack = []
    operations = ["+", "-", "/", "*"]
    for i in tokens:
        if i in operations:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(calculator(i, num1, num2))
        else:
            stack.append(int(i))
    return stack[0]