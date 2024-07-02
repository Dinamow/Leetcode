# Sign of the Product of an Array

## Problem Description

Given an array of integers `nums`, the sign of the product of all the numbers in the array is determined by the following rules:

- If the product is positive, the sign is `1`.
- If the product is negative, the sign is `-1`.
- If the product is zero, the sign is `0`.

You are required to implement the function `arraySign(nums: List[int]) -> int` that returns the sign of the product of `nums`.

## Example

```python
assert arraySign([-1,2,-3,-4,3,2,-1]) == 1
assert arraySign([1,5,0,2,-3]) == 0
assert arraySign([-1,1,-1,1,-1]) == -1
```

## Constraints

- `1 <= nums.length <= 1000`
- `-100 <= nums[i] <= 100`

