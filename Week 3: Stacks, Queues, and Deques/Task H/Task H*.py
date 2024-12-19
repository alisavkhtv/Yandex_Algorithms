n = int(input())
inputs = []
for i in range(n):
  new = str(input())
  inputs.append(new)
stack = []
prefsums = [0]
for i in inputs:
  if i.startswith('+'):
    value = int(i[1:])
    stack.append(value)
    prefsums.append(prefsums[-1]+value)
  elif i.startswith('?'):
    value = int(i[1:])
    top_sum = prefsums[-1] - prefsums[-1-value]
    print(top_sum)
  elif i.startswith('-'):
    top = stack.pop()
    prefsums.pop()
    print(top)
