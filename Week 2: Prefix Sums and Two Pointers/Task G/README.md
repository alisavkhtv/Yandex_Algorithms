# The Cencorship Product

### Time constraints: 2 secs
### Memory constraints: 256 Mb

### Description:
The Censorship Committee defined the rudeness of a string t_1 t_2 … t_k as the number of pairs of indices (i, j) where 1 ≤ i < j ≤ k, with t_i = "a" and t_j = "b". In other words, the rudeness of the string is the number of ways to strike out letters from it so that only the letters "a" and "b" remain (specifically in that order). Additionally, according to the same committee's decision, all literary works must be a substring of a certain string s defined by the committee, consisting of n letters.

Vasya wants to write a literary work whose rudeness does not exceed c. To do this, he must choose some non-empty substring of the string s, starting from index l and ending at index r, i.e., consisting of characters s_l s_(l+1) … s_r. The longer the work, the higher the payment, so Vasya wants his work to be as long as possible. Determine the length of the longest work that Vasya can write.

### Input:
The first line contains two integers n and c — the length of the string s and the maximum allowed rudeness of the literary work (1 ≤ n ≤ 10ˆ6, 0 ≤ c ≤ 10ˆ18). The second line contains the string s. The string consists of n lowercase English letters.

### Output:
Output the answer to the problem.
