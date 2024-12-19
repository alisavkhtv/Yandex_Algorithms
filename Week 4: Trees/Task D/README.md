# Binary Tree: INSERT, SEARCH, TRAVERSE

### Time constraints: 1 sec
### Memory constraints: 64 Mb

### Description:
Write a program that implements actions in a binary search tree: "insert" and "search" (by value). The program should handle three types of requests:
1. ADD n — If the specified number is not already in the tree, insert it and output the word "DONE". If it is already present, leave the tree unchanged and output the word "ALREADY".
2. SEARCH n — Output the word "YES" if the value is found in the tree, or "NO" if it is not found. The tree remains unchanged.
3. PRINTTREE — Output the entire tree using a specific format for displaying results.

### Input:
Each line of input contains one of the requests: ADD n, SEARCH n, or PRINTTREE. It is guaranteed that PRINTTREE requests will only be called when the tree is not empty. The total number of requests does not exceed 1000, with no more than 20 PRINTTREE requests.

### Output:
For each request, output the corresponding response. For ADD and SEARCH requests, print the appropriate word on a separate line. For PRINTTREE, output the tree according to the following algorithm:
1. Print the left subtree
2. Print a number of dots equal to the depth of the node
3. Print the key value
4. Print the right subtree
