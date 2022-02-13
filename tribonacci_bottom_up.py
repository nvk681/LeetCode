def tribonacci(n):
        if n <= 2:
            return 0 if n == 0 else 1
        values = [0]*(n+1)
        values[0] = 0 
        values[1] = 1
        values[2] = 1
        for index in range(3, n+1):
            values[index] = values[index-1]+values[index-2]+values[index-3]
        return values.pop()
print(tribonacci(4))
print(tribonacci(25))
# print(tribonacci())
# print(tribonacci())