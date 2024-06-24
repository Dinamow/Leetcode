class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        postion = 0
        for i in range(len(t)):
            if t[i] == s[postion]:
                if postion == len(s) - 1:
                    return True
                postion += 1
