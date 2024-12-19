# Count Descendants in a Geneology Tree

### Time constraints: 1 sec
### Memory constraints: 64 Mb

### Description:
In a genealogy tree, every person, except for the ancestor, has exactly one parent. Your task is to determine the number of all descendants for each element in the tree (excluding the element itself).

The program receives as input the number of elements in the genealogy tree N. Following this, there are N−1 lines that specify the parent for each element of the tree, except for the ancestor. Each line has the format descendant parent.

The output should list all elements in lexicographical order, and for each element, you should print the number of its descendants.

### Input:
The first line contains an integer N (1 ≤ N ≤ 100000) — the number of elements in the genealogy tree. The next N−1 lines contain pairs of names: descendant parent.

### Output:
Output each element's name followed by the number of its descendants in lexicographical order.
