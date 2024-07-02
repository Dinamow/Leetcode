from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        value = 1
        for number in nums:
            value *= number
        if value > 0:
            return 1
        if value < 0:
            return -1
        return 0

