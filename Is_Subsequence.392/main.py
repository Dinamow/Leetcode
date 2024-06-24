from sloution import Solution

engine = Solution()
s = "abc"
t = "ahbgdc"

assert engine.isSubsequence(s, t)

s = "axc"
t = "ahbgdc"

assert not engine.isSubsequence(s, t)

print("All tests passed.")

