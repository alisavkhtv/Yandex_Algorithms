# A Minimum on an Interval

### Time constraints: 1 sec
### Memory constraints: 64 Mb

### Description:
Consider a sequence of integers of length n. A "window" of length k moves along the sequence with a step of 1, meaning that initially, the first k numbers are visible in the window, and in the next step, the window will show the k numbers starting from the second element, and so on until the end of the sequence. The task is to determine the minimum value within each position of the window.

### Input:
The first line contains two natural numbers n and k (n ≤ 150000, k ≤ 10000, k ≤ n) — the lengths of the sequence and the window, respectively. The following line contains n integers — the sequence itself.

### Output:
The output should contain n − k + 1 lines — the minimum values for each position of the window.
