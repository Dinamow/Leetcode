# Baseball Game

## Description

This is a solution for the "Baseball Game" problem on LeetCode.

## Problem Statement

You are keeping score for a baseball game. The game consists of several rounds, where the scores of each round are represented by a list of strings.

Each string can be one of the following:

- An integer, which represents the number of points scored in this round.
- "+" (which represents that the points scored in this round are the sum of the last two valid round's points).
- "D" (which represents that the points scored in this round are double the last valid round's points).
- "C" (which represents that the last valid round's points are invalid and should be removed).

You need to return the sum of the points scored for all the valid rounds.

## Example

Input: ["5","2","C","D","+"]

Output: 30

Explanation: 

Round 1: You could get 5 points. The sum is: 5.

Round 2: You could get 2 points. The sum is: 7.

Operation 1: The round 2's data was invalid. The sum is: 5.

Round 3: You could get 10 points (the round 2's data have been removed). The sum is: 15.

Round 4: You could get 5 + 10 = 15 points. The sum is: 30.

## Constraints

- The number of rounds is between 1 and 1000.
- Each round's score is an integer between -30000 and 30000.

