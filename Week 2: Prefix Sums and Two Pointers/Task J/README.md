# Investigation of Evidence

### Time constraints: 2 secs
### Memory constraints: 256 Mb

### Description:
Benoit Blanc has taken on the investigation of a mysterious crime and is now actively searching for evidence that will help him identify the real criminal. Like any self-respecting detective, Benoit Blanc has his own method of seeking the truth. As he likes to repeat, his philosophy is that one can simply be a passive observer, and life will lead you to the truth.

In total, Benoit Blanc has gathered n pieces of evidence and arranged them in a row. The i-th piece of evidence has a weight denoted by a_i. The detective believes that the least weighted pieces of evidence might be the most interesting, and he has developed the following process for their investigation.

First, Blanc selects a piece of evidence with number x and begins to examine the pieces to the left of it. While there is a piece of evidence to the left with a weight less than or equal to the current piece, Benoit Blanc moves to it. However, the eccentric detective quickly becomes bored with monotony, so he will not make more than k moves between pieces with the same weight.

For example, if the weights of the pieces of evidence are ⟨3, 3, 3, 4, 4, 5⟩, with k = 2, and the detective starts from the last piece, he will make four moves to the left before stopping.

The pieces of evidence require careful examination, so Benoit Blanc repeats this process m times, starting from the piece of evidence numbered x_i in the i-th iteration. Help him quickly determine which piece of evidence he will stop at in each case.

### Input:
The first line contains an integer n — the number of pieces of evidence (1 ≤ n ≤ 4*10ˆ5). The second line contains n integers separated by spaces: a_i — the weights of the pieces of evidence in their order (1 ≤ a_i ≤ 10ˆ9). The next line contains two integers separated by space: m and k — the number of experiments and the maximum number of moves between pieces with equal weight (1 ≤ m ≤ 4*10ˆ5; 0 ≤ k ≤ n). The last line contains m integers separated by spaces: x_i — the indices of the pieces of evidence from which Benoit Blanc will start his investigation (1 ≤ x_i ≤ n.

### Output:
Output m integers from 1 to n separated by spaces; each integer should represent the index of the piece of evidence where the detective will stop in each experiment. 
