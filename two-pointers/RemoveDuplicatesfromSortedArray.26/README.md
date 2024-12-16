# Remove Duplicates from Sorted Array

## Problem Description
Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

### Requirements
1. Modify the array `nums` such that the first `k` elements contain the unique elements in the original order.
2. Return the value of `k`, the number of unique elements.
3. The remaining elements in the array beyond the first `k` are not important.

### Custom Judge
The judge will test your implementation with the following code:

```java
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```
If all assertions pass, your solution will be accepted.

---

## Examples

### Example 1
**Input:**
```text
nums = [1,1,2]
```
**Output:**
```text
2, nums = [1,2,_]
```
**Explanation:**
Your function should return `k = 2`, with the first two elements of `nums` being `[1, 2]`. The underscores (`_`) represent values that don't matter.

### Example 2
**Input:**
```text
nums = [0,0,1,1,1,2,2,3,3,4]
```
**Output:**
```text
5, nums = [0,1,2,3,4,_,_,_,_,_]
```
**Explanation:**
Your function should return `k = 5`, with the first five elements of `nums` being `[0, 1, 2, 3, 4]`. The underscores (`_`) represent values that don't matter.

---

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in **non-decreasing order**.

---

## Solution Approach

### Algorithm
1. Use a two-pointer approach:
   - `i` to track the position of the current unique element.
   - `j` to iterate through the array.
2. Compare `nums[j]` with `nums[i]`. If they are different, increment `i` and update `nums[i]` to `nums[j]`.
3. Return `i + 1` as the count of unique elements.

### Code Implementation

#### Python
```python
def removeDuplicates(nums):
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1
```

#### Java
```java
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;

    int i = 0;
    for (int j = 1; j < nums.length; j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}
```

---

## Key Takeaways
- The problem demonstrates the **two-pointer technique**, which is efficient for in-place modifications.
- The algorithm runs in **O(n)** time and uses **O(1)** extra space.
- It leverages the sorted property of the array to identify duplicates easily.

---

## Practice Challenge
Try modifying the algorithm to handle an unsorted array. How would you approach the problem if the array was not sorted?

---

## Resources
- [Two-Pointer Technique Explanation](https://en.wikipedia.org/wiki/Two-pointer_technique)
- [In-Place Array Modifications](https://www.geeksforgeeks.org/in-place-algorithm/)

---

### Author
This README is part of a learning exercise to understand array manipulation and in-place algorithms.


