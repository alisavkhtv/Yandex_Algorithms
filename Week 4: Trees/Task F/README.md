# Bureaucracy

### Time constraints: 3 secs
### Memory constraints: 256 Mb

### Description:
Mirko has become the CEO of a large corporation. The company employs N people, numbered from 1 to N, with Mirko being number 1. Everyone except Mirko has a boss. A boss can have multiple subordinates, but no more than one direct supervisor.

When Mirko receives a task from investors, he passes it to his subordinate with the smallest number. This subordinate then passes it to their subordinate with the smallest number, and so on, until the task reaches an unfortunate employee without subordinates, who must complete the task.

This employee receives 1 coin, their boss receives 2 coins, the boss of that boss receives 3 coins, and so forth. Then the employee who actually did the work realizes how unfair this capitalist system is and quits their job.

Mirko continues to receive tasks until only one employee remains in the corporation—himself. At that point, he completes the task, receives 1 coin, and leaves the corporation. He is curious about how many coins each former employee received. Help him with this.

### Input:
The first line contains a single natural number N (1 ≤ N ≤ 2*10ˆ5) — the number of employees in the company. The following line contains N−1 numbers a_2, a_3, ..., a_N (1 ≤ a_i < i), where a_i is the number of the boss of employee i.

### Output:
Output N numbers; the i-th number should indicate how many coins employee i received.
