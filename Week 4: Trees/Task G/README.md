# Woodpeckers

### Time constraints: 10 secs
### Memory constraints: 512 Mb

### Description:
In the park, there are two very tall trees, each with hollows located one below the other at equal distances. One day, N woodpeckers decided to inhabit these hollows. Some of them are acquainted and would like to be able to visit each other. The woodpeckers fly in straight lines and very quickly. To reduce the likelihood of collisions, they decided to settle according to the following principle:
- Each pair of woodpeckers who wish to visit each other must live on different trees. The segments connecting the hollows of acquainted woodpeckers do not intersect (although their endpoints may coincide).
- Additionally, the woodpeckers want to live as low as possible, meaning that on each tree they occupy consecutive hollows starting from the bottom. There are more hollows on each tree than the total number of woodpeckers.

As it is known, woodpeckers have very small brains. Therefore, you should think for them and inform how many ways they can be arranged in the hollows. Since woodpeckers also have difficulty processing large numbers, the answer should be given modulo K.

### Input:
The first line contains three numbers:
- N — the number of woodpeckers (1 ≤ N ≤ 10ˆ6)
- M — the number of pairs of acquainted woodpeckers (1 ≤ M ≤ 10ˆ7)
- K — the number to take modulo (1 ≤ K ≤ 2*10ˆ6)

The next M lines contain two numbers a_i and b_i (1 ≤ a_i, b_i ≤ N), representing a pair of acquainted woodpeckers.

### Output:
The output should contain a single number: the number of arrangements modulo K.
