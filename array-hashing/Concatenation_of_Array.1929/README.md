## Concatenation of Array

Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where `ans[i]` is equal to `nums[i]` and `ans[i + n]` is equal to `nums[i]` for `0 <= i < n` (0-indexed).

Specifically, `ans` is the concatenation of two `nums` arrays.

### Example

**Input:**
```python
nums = [1,2,1]
```

**Output:**
```python
[1,2,1,1,2,1]
```

**Explanation:**
The array `ans` is formed as follows:
- `ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]`
- `ans = [1,2,1,1,2,1]`

### Constraints

- `n == nums.length`
- `1 <= n <= 1000`
- `1 <= nums[i] <= 1000`
