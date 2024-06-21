"""
This module contains a solution for the problem of,
determining whether an array contains any duplicates.

The Solution class provides a method called containsDuplicate,
that takes in an array of integers and returns a boolean value,
indicating whether the array contains any duplicates.

Example usage:
    nums = [1, 2, 3, 1]
    solution = Solution()
    print(solution.containsDuplicate(nums))  # Output: True
"""

from typing import List


class Solution:
    """
    A class that provides a method to determine whether,
    an array contains any duplicates.
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Determines whether an array contains any duplicates.

        Args:
            nums (List[int]): The array of integers.

        Returns:
            bool: True if the array contains duplicates, False otherwise.
        """
        # for number in nums:
        #     if nums.count(number) > 1:
        #         return True
        # return False
        # -------------------------------------
        return len(set(nums)) != len(nums)
        # -------------------------------------
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False
