# Reverse String

## Problem Description

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must reverse the array in-place using O(1) extra memory.

## Requirements

- Modify the input array `s` directly such that the characters are reversed.
- Do not use any additional arrays or memory beyond a constant amount (O(1) space).
- The function should operate efficiently in O(n) time complexity.

## Examples

### Example 1

**Input:**

```python
s = ["h", "e", "l", "l", "o"]
```

**Output:**

```python
["o", "l", "l", "e", "h"]
```

### Example 2

**Input:**

```python
s = ["H", "a", "n", "n", "a", "h"]
```

**Output:**

```python
["h", "a", "n", "n", "a", "H"]
```

## Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is a printable ASCII character.

## Solution Approach

### Algorithm

The problem can be efficiently solved using the two-pointer technique:

1. Initialize two pointers:
    - `left` starting at the beginning of the array (0).
    - `right` starting at the end of the array (len(s) - 1).
2. Swap the characters at `left` and `right`.
3. Move the pointers closer to each other:
    - Increment `left` by 1.
    - Decrement `right` by 1.
4. Repeat steps 2-3 until `left` is greater than or equal to `right`.

### Code Implementation

```python
def reverseString(s: list[str]) -> None:
     """
     Reverses the input array of characters in-place.
     """
     left, right = 0, len(s) - 1
     
     while left < right:
          # Swap the characters
          s[left], s[right] = s[right], s[left]
          left += 1
          right -= 1
```

## How It Works

| Step | Array State            | Left Pointer | Right Pointer |
|------|-------------------------|--------------|---------------|
| Init | ["h", "e", "l", "l", "o"] | 0            | 4             |
| 1    | ["o", "e", "l", "l", "h"] | 1            | 3             |
| 2    | ["o", "l", "l", "e", "h"] | 2            | 2             |

At this point, `left` meets `right`, and the array is fully reversed.

## Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the array. Each character is swapped at most once.
- **Space Complexity:** O(1) since no extra memory is used apart from a few variables.

## Key Takeaways

- The two-pointer technique is an efficient approach for in-place array modifications.
- Understanding in-place algorithms helps optimize memory usage.
- This problem highlights the importance of O(1) space constraints in large-scale systems.

## Practice Challenge

Try modifying the algorithm to reverse only a portion of the array. For example, reverse the characters between two given indices `left` and `right`.

## Resources

- [Two-Pointer Technique](https://en.wikipedia.org/wiki/Two-pointer_technique)
- [In-Place Algorithms](https://en.wikipedia.org/wiki/In-place_algorithm)

## Author

This README is part of a learning exercise to understand in-place algorithms and two-pointer techniques.
