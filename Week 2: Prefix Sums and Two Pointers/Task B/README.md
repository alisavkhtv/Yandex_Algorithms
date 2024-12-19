# The Sum of Numbers

### Time constraints: 1 sec
### Memory constraints: 64 Mb

### Description:
Vasya really loves to look for his lucky number K everywhere. Every day he walks to school along a street where N cars are parked. He became interested in how many sets of cars parked consecutively from positions L to R have a sum of their numbers equal to K. Help Vasya find the answer to his question.

For example, if N = 5, K = 17, and the car numbers are 17, 7, 10, 7, 10, then there are 4 sets of cars:
- 17 (L = 1, R = 1)
- 7, 10 (L = 2, R = 3)
- 10, 7 (L = 3, R = 4)
- 7, 10 (L = 4, R = 5)

### Input:
In the first line of input data, the numbers N and K are given (1 ≤ N ≤ 10ˆ6, 1 ≤ K ≤ 10ˆ9). The second line contains N integers that represent the car numbers. The car numbers can take values from 1 to 999 inclusive.

### Output:
You need to output a single number — the count of sets.
