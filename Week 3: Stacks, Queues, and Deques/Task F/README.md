# Minimum Lexicographic Valid Sequence of Parentheses

### Time constraints: 1 sec
### Memory constraints: 64 Mb

### Description:
Let's recall the definition of a valid parenthesis sequence (VPS):
- An empty string is a valid parenthesis sequence
- A valid parenthesis sequence enclosed in one type of brackets is also a valid parenthesis sequence
- A valid parenthesis sequence to which another valid parenthesis sequence is appended on the left or right is also a valid parenthesis sequence

Given that the symbols [, ], (, and ) are ordered in a specific way, we need to find the lexicographically minimal valid parenthesis sequence of length n that starts with the string s. A string A is lexicographically smaller than string B (of equal length) if there exists an index i such that for all j < i, A[j] = B[j] and A[i] < B[i].

### Input:
The first line contains an integer n (1 ≤ n ≤ 100000). The second line contains a string w consisting of 4 distinct bracket characters that define their lexicographic order. The third line contains a string s, whose length does not exceed n.

### Output:
Output the lexicographically minimal valid parenthesis sequence of length n that starts with s.
