from solution import Solution

engine = Solution()

s = "Hello World"

assert engine.lengthOfLastWord(s) == 5

s = "   fly me   to   the moon  "

assert engine.lengthOfLastWord(s) == 4

s = "luffy is still joyboy"

assert engine.lengthOfLastWord(s) == 6


print("Passed")

