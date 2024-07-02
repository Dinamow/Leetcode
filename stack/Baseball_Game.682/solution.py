from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for letter in operations:
            if letter == "D":
                stack.append(int(stack[-1] * 2))
            elif letter == "+":
                stack.append(int(stack[-1] + stack[-2]))
            elif letter == "C":
                stack.pop(-1)
            else:
                stack.append(int(letter))
        return sum(stack)

