from solution import Solution

engine = Solution()

strs = ["flower","flow","flight"]

assert engine.longestCommonPrefix(strs) == "fl"

strs = ["dog","racecar","car"]

assert engine.longestCommonPrefix(strs) == ""

print("All Passed!")
