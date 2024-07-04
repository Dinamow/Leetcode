# Top K Frequent Elements

This repository contains the solution for the "Top K Frequent Elements" problem on LeetCode.

## Problem Description

Given a non-empty array of integers, find the top k elements which have the highest frequency in the array. Return the k most frequent elements.

## Solution Approach

To solve this problem, we can use a combination of a hash map and a priority queue. First, we iterate through the array and count the frequency of each element using a hash map. Then, we insert the elements into a priority queue based on their frequency. Finally, we extract the top k elements from the priority queue and return them as the result.

## Time Complexity

The time complexity of this solution is O(n log k), where n is the number of elements in the array and k is the given value.

## Space Complexity

The space complexity of this solution is O(n), where n is the number of elements in the array.
