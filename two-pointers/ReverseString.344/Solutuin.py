from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        firstIndex = 0
        lastIndex = len(s) - 1
        while lastIndex > firstIndex and firstIndex < len(s) and lastIndex > 0:
            s[firstIndex], s[lastIndex] = s[lastIndex], s[firstIndex]
            firstIndex += 1
            lastIndex -= 1
            print(f"{firstIndex}: {s}")
