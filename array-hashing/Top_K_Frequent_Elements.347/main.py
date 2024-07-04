from solution import Solution

engine = Solution()

assert engine.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]

assert engine.topKFrequent([1], 1) == [1]

print('All tests passed')

