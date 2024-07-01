from solution import Solution

engine = Solution()

assert engine.findDifference([1, 2, 3], [2, 4, 6]) == [[1, 3], [4, 6]]

assert engine.findDifference([1, 2, 3, 3], [1, 1, 2, 2]) == [[3], []]

print("All tests passed!")

