class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        nums = []
        
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                nums.append("FizzBuzz")
            elif i % 5 == 0:
                nums.append("Buzz")
            elif i % 3 == 0:
                nums.append("Fizz")
            else:
                nums.append(str(i))
                
        return nums