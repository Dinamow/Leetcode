from solution import Solution

engine = Solution()

assert engine.calPoints(["5", "2", "C", "D", "+"]) == 30

assert engine.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27

assert engine.calPoints(["1", "C"]) == 0

print("All tests passed!")

