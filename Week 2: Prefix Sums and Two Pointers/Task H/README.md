# Relocation to Open Space*

### Time constraints: 1 sec
### Memory constraints: 256 Mb

### Description:
Employees of the company work in an old Soviet building consisting of n large offices arranged in a row, one after another. In room i, there are exactly a_i employees. 

The HR managers of the company found that employees feel sad and lonely in separate offices, and to make them happier, it is necessary to convert one of the offices into a trendy open space and relocate all employees there.

Relocating an employee to another office involves moving their desk, which is quite difficult and time-consuming. When relocating, an employee moves their desk through all offices from their initial position to the open space office. Thus, the number of transitions for an employee is defined as the absolute difference between the numbers of their original office and the office equipped with the open space. The HR managers want to make the move as easy as possible by choosing an office for the open space that minimizes the total number of transitions for all employees (and their desks). Help them determine this number of transitions.

### Input:
The first line contains a single integer n — the number of offices in the company (1 ≤ n ≤ 2*10ˆ5). The next line lists n integers a_i — the number of employees in office i (1 ≤ a_i ≤ 10ˆ9).

### Output:
Output a single integer — the minimum total number of transitions.
