# Valid Parentheses

## Problem Description

Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

## Examples

**Example 1:**

Input: `()`
Output: `true`

**Example 2:**

Input: `()[]{}`
Output: `true`

**Example 3:**

Input: `(]`
Output: `false`

**Example 4:**

Input: `([)]`
Output: `false`

**Example 5:**

Input: `{[]}`
Output: `true`

## Approach

To solve this problem, we can use a stack data structure. We iterate through the characters of the input string and for each character, we check if it is an opening bracket. If it is, we push it onto the stack. If it is a closing bracket, we check if the stack is empty or if the top of the stack is not the corresponding opening bracket. If either of these conditions is true, we return `false`. Otherwise, we pop the top element from the stack.

After iterating through all the characters, if the stack is empty, it means all the opening brackets have been closed in the correct order, so we return `true`. Otherwise, we return `false`.

## Complexity Analysis

The time complexity for this approach is O(n), where n is the length of the input string. This is because we iterate through each character of the string once. The space complexity is also O(n), as the stack can contain at most n/2 elements in the worst case scenario.
