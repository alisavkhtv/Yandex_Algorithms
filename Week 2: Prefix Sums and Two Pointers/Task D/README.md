# The Best Form of Rest

### Time constraints: 2 secs
### Memory constraints: 256 Mb

### Description:
Vasya has to complete n tasks, and for each task, he has defined a direction of activity represented by an integer a_i. In one day, Vasya can do any number of tasks, but he believes that the best form of rest is to change activities. Therefore, he does not want to perform similar tasks on the same day. Tasks with numbers a_i and a_j are considered similar if the difference between their numbers does not exceed a given diversity coefficient k, that is, if ∣a_i − a_j∣ ≤ k. Vasya also wants to complete all his tasks as quickly as possible. For example, if Vasya needs to complete three tasks with activity directions 1, 2, and 4 with k = 2, then on the first day he can do tasks 1 and 4, and on the second day he can do task 2. He cannot complete all tasks in one day because the activity directions 1 and 2 are similar.

Determine the minimum number of days required for Vasya to complete all his tasks.

### Input:
The first line contains two integers separated by space: n and k — the number of tasks and the diversity coefficient (1 ≤ n ≤ 2*10ˆ5; 0 ≤ k ≤ 10ˆ9). The second line lists n integers separated by space: a_i — the directions of the tasks (1 ≤ a_i ≤ 10ˆ9).

### Output:
Output a single integer — the minimum number of days required for Vasya to complete all his tasks.
