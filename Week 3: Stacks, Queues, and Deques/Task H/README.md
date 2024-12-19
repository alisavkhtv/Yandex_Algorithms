# Stack with a Sum*

### Time constraints: 1 sec
### Memory constraints: 256 Mb

### Description:
The stack with sum must support three operations:
1. Add a number x to the stack.
2. Calculate and output the sum of the top k numbers in the stack.
3. Remove a number from the stack.
You need to implement a data structure that supports these operations.

### Input:
The first line contains an integer n — the number of stack operations (1 ≤ n ≤100000). The following n lines describe the stack operations. Each operation is one of three types:
- + x — add the number x to the stack (1 ≤ x ≤ 10ˆ9)
- - — remove the top element from the stack (it is guaranteed that the stack is not empty at this moment)
- ? k — calculate and output the sum of the top k elements in the stack (it is guaranteed that there are at least k elements in the stack).

Initially, the stack is empty.

### Output:
For each - query, you need to output the value of the removed element, and for each ? k query, you need to output the sum of the top k elements in the stack.
