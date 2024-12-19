# Automated Warehouse

### Time constraint: 1 sec
### Memory constraint: 256 Mb

### Description:
The warehouse consists of a set of identical squares surrounded by driveways. At the corners of each square, there are intersections formed by intersecting driveways at right angles.

Rovers move through the warehouse and follow these rules at intersections:
1. At an intersection with unequal roads, a rover on a secondary road must yield to a rover approaching from the main road.
2. If the main road at the intersection changes direction, rovers on the main road must follow the rules for equal roads among themselves.
3. At an intersection with equal roads, a rover must yield to vehicles approaching from the right.

For testing, a specific intersection has been chosen where it is necessary to determine the order in which N rovers will pass through, approaching the intersection from each of the four sides at given times. The sides are numbered 1, 2, 3, and 4 in a clockwise manner. It is known that at most one rover arrives from each side of the intersection per unit of time, and all rovers adhere to the rules and do not overtake each other. Since this is just the beginning of testing, all rovers want to pass straight through the intersection. Rovers approaching from sides a and b are on the main road; others are on secondary roads. It takes one unit of time for a rover to pass through the intersection.

Thus, a rover can only pass through the intersection if:
- There are no rovers ahead of it in line to pass through
- There are no rovers that it needs to yield to
If two rovers at the front of the queue do not need to yield to each other, they will pass through the intersection simultaneously.

Determine the order in which the rovers will pass through the intersection.

### Input:
The first line of the input file contains a single integer N (1 ≤ N ≤ 100) — the number of rovers. The second line contains integers a and b — the sides of the intersection that make up the main road (1 ≤ a, b ≤ 4; a ≠ b).

Each of the following N lines contains a description of a rover consisting of two integers d_i and t_i (1 ≤ d_i ≤ 4; 1 ≤ t_i ≤ 100) — the direction and arrival time of the i-th rover.

### Output:
In the output file, print N integers, one per line. The i-th line should contain the time at which the i-th rover passes through the intersection. The rovers are numbered in order of their appearance in the input file.

