n = int(input())
matrix = [list(input().strip()) for _ in range(n)]

def transpose_matrix(x):
    return [list(row) for row in zip(*x)]

def del_row(x):
    leave_rows = []
    for row in range(len(x)):
        if row == 0:
          leave_rows.append(x[row])
        else:
          if x[row] != leave_rows[-1]:
            leave_rows.append(x[row])
    return leave_rows

def del_col(x):
    transposed = list(zip(*x))
    leave_cols = del_row(transposed)
    return transpose_matrix(leave_cols)

def final(x):
    while True:
        adj_x = del_row(x)
        adj_x = del_col(adj_x)
        if adj_x == x:
            break
        x = adj_x
    return x

def to_del(x):
  n = len(x)
  y = transpose_matrix(x)
  m = len(y)
  row = 0
  while row < m:
    if y[row] == list(n*'.'):
      if row == 0:
        del y[row]
        m -= 1
        row = 0
      elif row == m-1:
        del y[row]
        m -= 1
        row -= 1
      else:
        row += 1
    else:
      row += 1
  return y

testing_i = to_del(matrix)
tested_i = to_del(testing_i)
final_ = final(tested_i)
final__=transpose_matrix(final_)

if len(final_) == 2 and len(final__) == 2 and final__[0] == list(len(final_)*'#') and final__[1][0] == '.':
  print('L')
elif len(final_) == 1 and len(final__) == 1 and final_[0] == ['#']:
  print('I')
elif len(final_) == 3 and len(final__) == 2 and final__[0] == list(len(final_)*'#'):
  print('C')
elif len(final_) == 3 and len(final__) == 3 and final__[0] == list(len(final_)*'#') and final__[-1] == list(len(final_)*'#') and final__[1][1] == '.':
  print('O')
elif len(final_) == 3 and len(final__) == 3 and final__[0] == list(len(final_)*'#') and final__[-1] == list(len(final_)*'#') and final__[1][0] == '.':
  print('H')
elif len(final_) == 4 and len(final__) == 3 and final__[0] == list(len(final_)*'#') and final__[1] == ['#', '.', '#', '.'] and final__[-1] == ['#', '#', '#', '.']:
  print('P')
else:
  print('X')
