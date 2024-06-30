#!/usr/bin/env python3
from solution import Solution

engine = Solution()

assert engine.majorityElement([3, 2, 3]) == 3

assert engine.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2

print("Passed all tests!")
