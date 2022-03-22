class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            div_by_3 = False if i%3 != 0 else True
            div_by_5 = False if i%5 != 0 else True 
            if div_by_3 and div_by_5:
                result.append("FizzBuzz")
                continue
            if div_by_3:
                result.append("Fizz")
                continue
            if div_by_5:
                result.append("Buzz")
                continue
            result.append(str(i))
        return result