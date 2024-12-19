# Studying Algorithms*

### Time constraints: 1 sec
### Memory constraints: 256 Mb

### Description:
Vasya is preparing for the algorithmic section of an interview and has found that he needs to study n algorithms. He has superficially studied each of them and characterized the i-th algorithm with two parameters: 
- a_i (interestingness)
- b_i (usefulness)

Vasya works as a system administrator at a research base in Antarctica and is in no hurry. He will study one algorithm per day. If he is bored, he will study the most interesting algorithm (with the maximum a_i) from all the algorithms that have not yet been studied. If he is in an inspired mood, he will choose to study the most useful algorithm (with the maximum b_i) from those that are still available.

If there are multiple algorithms with the maximum interestingness, he will choose the one with the highest usefulness. If the usefulness values are also equal, he will choose the algorithm with the smallest index.

Vasya is a predictable person (and is proud of it), so he knows his mood for the next n days in advance. Determine the order in which he will study the algorithms.

### Input:
The first line contains a single integer n — the number of algorithms (1 ≤ n ≤ 10ˆ5). The second line contains n integers a_i — the interestingness values of the algorithms (1 ≤ a_i ≤ 10ˆ9). The third line contains n integers b_i — the usefulness values of the algorithms (1 ≤ b_i ≤ 10ˆ9). The last line contains n integers p_i — indicators of Vasya's mood for the next n days. If p_i = 1, Vasya will choose the algorithm with maximum usefulness (maximum b_i); otherwise, if p_i = 0, he will choose the most interesting available algorithm (maximum a_i).

### Output:
Output n distinct integers from 1 to n separated by spaces; the i-th number should be equal to the index of the algorithm that Vasya will study on day i.
