# The raft

![alt text](https://contest.yandex.ru/testsys/statement-file?hash=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..WtKkj8X7L1KKeLXV.ilJsL-F4DtGaoTnb-iKpX7VgxjtDYJMcRBVaQowX7OJGc9OXdPmI7PqbrKZBHdU7bGmlDfHSdm8swi2FoIah7_MUbLdjlw.Lpa_elDg5pSI4XVyggoxMQ)

### Description:
In the middle of the lake, there is a raft shaped like a rectangle. The sides of the raft are aligned along parallels and meridians. Let's introduce a coordinate system where the OX axis points east and the OY axis points north. Let the southwest corner of the raft have coordinates (x_1, y_1), and the northeast corner have coordinates (x_2, y_2).

A swimmer is located at a point with coordinates (x,y). Determine which side of the raft (north, south, west, or east) or which corner of the raft (northwest, northeast, southwest, or southeast) the swimmer should swim towards to reach the raft as quickly as possible.

### Input constraints
The program receives six numbers as input in the following order:
- x_1, y_1 (coordinates of the southwest corner of the raft)
- x_2, y_2 (coordinates of the northeast corner of the raft)
- x, y (coordinates of the swimmer)

All numbers are integers and do not exceed 100 in absolute value. It is guaranteed that x_1 < x_2, y_1 < y_2, x != x_1, x != x_2, y != y_1, y != y_2. Thus, the swimmer's coordinates are outside the raft.

### Output requirements
