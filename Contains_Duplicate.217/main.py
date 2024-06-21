"""
This script tests the functionality of the `containsDuplicate`,
method in the `Solution` class.

The `containsDuplicate` method takes in a list of integers and returns True,
if the list contains any duplicate elements, and False otherwise.
"""

from sloution import Solution

s = Solution()

nums = [1, 2, 3, 1]

assert s.containsDuplicate(nums)

nums = [1, 2, 3, 4]

assert not s.containsDuplicate(nums)

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

assert s.containsDuplicate(nums)
