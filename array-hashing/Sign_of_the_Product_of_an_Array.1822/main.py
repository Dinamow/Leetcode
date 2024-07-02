from solution import Solution

engine = Solution()

assert engine.arraySign([-1,-2,-3,-4,3,2,1]) == 1

assert engine.arraySign([1,5,0,2,-3]) == 0

assert engine.arraySign([-1,1,-1,1,-1]) == -1

print("Passed all tests!")

