# Majority Element

## Problem Statement

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

### Examples

- **Example 1:**

  - Input: `nums = [3,2,3]`
  - Output: `3`

- **Example 2:**

  - Input: `nums = [2,2,1,1,1,2,2]`
  - Output: `2`

### Constraints

- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

### Follow-up

Could you solve the problem in linear time and in O(1) space?

## Solution Approach

The problem can be solved using the Boyer-Moore Voting Algorithm, which operates in linear time (`O(n)`) and constant space (`O(1)`). The essence of this algorithm is to find a candidate for the majority element and then verify if it is indeed the majority element.

### Boyer-Moore Voting Algorithm

1. **Initialize two variables:**
   - A candidate variable to store the element that might be the majority element.
   - A count variable to keep track of the candidate's occurrence.

2. **First Pass:**
   - Iterate through the array.
   - If the count is 0, assign the current element as the candidate.
   - If the current element is the candidate, increment the count. Otherwise, decrement the count.

3. **Second Pass (Optional):**
   - Verify that the candidate is the majority element by counting its occurrences in the array. This step is optional since the problem statement guarantees the existence of a majority element.

### Implementation

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate, count = num, 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
```
