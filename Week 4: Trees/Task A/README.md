# Height of the Genealogy Tree

### Time constraints: 1 sec
### Memory constraints: 64 Mb

### Description:
In a genealogy tree, every person, except for the ancestor, has exactly one parent. Each element of the tree is associated with a non-negative integer called height. The ancestor has a height of 0, and any other element has a height that is one greater than that of its parent. Given a genealogy tree, your task is to determine the height of all its elements.
The program receives as input the number of elements in the genealogy tree N. Following this, there are N−1 lines that specify the parent for each element of the tree, except for the ancestor. Each line has the format descendant parent.

The program should output a list of all elements in lexicographical order. After printing the name of each element, you should also print its height.

### Input:
The first line contains an integer N (1 ≤ N ≤ 100000) — the number of elements in the genealogy tree. The next N−1 lines contain pairs of names: descendant parent.

### Output:
Output each element's name followed by its height in lexicographical order.
