# Queue at the Pick-up Point

### Time constraints: 2 secs
### Memory constraints: 512 Mb

### Description:
The service point operates for n minutes, numbered from 1 to n. At the beginning of the i-th minute, a_i clients will enter the service point and all of them will queue at the end. During one minute, the service point can serve no more than b clients — if there are at least b clients in the queue, then the first b of them are served; otherwise, all clients in the queue are served. All clients served at the end of the i-th minute will leave the service point at that time. At the end of the n-th minute, the service point will close. All clients who have not been served will wait for one more minute, complaining, and then leave. Calculate the total time all clients spend at the service point.

Note that if a client enters the service point at the beginning of the i-th minute and leaves at the end of that minute, they spent one minute at the service point.

### Input:
The first line contains two integers n and b — the number of minutes the service point operates and the number of clients that can be served in one minute (1 ≤ n ≤ 100000; 1 ≤ b ≤ 10ˆ8). The second line contains n integers a_i  — the number of clients arriving at the service point at the beginning of the i-th minute (0 ≤ a_i ≤ 10ˆ8).

### Output:
Output a single integer — the total time all clients spend at the service point.
