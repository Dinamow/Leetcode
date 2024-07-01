from solution import Solution

engine = Solution()

nums = [1, 7, 3, 6, 5, 6]

assert engine.pivotIndex(nums) == 3

nums = [1, 2, 3]

assert engine.pivotIndex(nums) == -1

nums = [2, 1, -1]

assert engine.pivotIndex(nums) == 0


print("Passed all tests!")

