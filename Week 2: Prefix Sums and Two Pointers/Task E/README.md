# Delete medians

### Time constraints: 2 secs
### Memory constraints: 256 Mb

### Description:
You are given a sequence of numbers a_i of length n. You need to sequentially remove the medians from it. The median in this task is defined as follows:
- If the number of elements in the sequence is odd, the median is the number that stands exactly in the middle of the sorted sequence
- If the number of elements in the sequence is even, the median of the sequence is:
- - the smaller of the two middle numbers in the sorted sequence if the two middle numbers are different.
  - Any of the two middle numbers if they are equal.

Determine the order in which elements will be removed from the sequence.

### Input:
The first line contains one natural number n — the number of elements in the sequence (1 ≤ n ≤ 10ˆ5). The second line contains n natural numbers a_i — the elements of the sequence (1 ≤ a_i ≤ 10ˆ9).

### Output:
Output n numbers — the order in which numbers are removed from the sequence.
