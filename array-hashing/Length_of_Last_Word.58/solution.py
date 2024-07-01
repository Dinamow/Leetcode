class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s or len(s) < 1:
            return 0
        num = 0
        postion = -1
        while True:
            if s[postion] == ' ' and num == 0:
                postion -= 1
            elif s[postion] != ' ':
                num += 1
                postion -= 1
                if postion < (len(s) * -1):
                    break
            elif s[postion] == ' ':
                break
        return num

