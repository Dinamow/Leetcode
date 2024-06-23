from sloution import Solution

engine = Solution()

nums = [1, 2, 1]

assert engine.getConcatenation(nums) == [1, 2, 1, 1, 2, 1]

nums = [1, 3, 2, 1]

assert engine.getConcatenation(nums) == [1, 3, 2, 1, 1, 3, 2, 1]

print("All passed")