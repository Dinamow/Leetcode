from solution import Solution

engine = Solution()

assert engine.isValid("()")

assert engine.isValid("()[]{}")

assert not engine.isValid("(]")

assert not engine.isValid("([)]")

assert engine.isValid("{[]}")

print("Passed all tests!")

