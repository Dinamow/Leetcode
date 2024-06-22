from sloution import Solution

engine = Solution()

s = "anagram"
t = "nagaram"

assert engine.isAnagram(s, t)

s = "rat"
t = "car"

assert not engine.isAnagram(s, t)

print("All Testes passed!")