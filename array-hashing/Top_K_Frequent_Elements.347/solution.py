from Typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
    
        sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        return [item[0] for item in sorted_freq[:k]]

