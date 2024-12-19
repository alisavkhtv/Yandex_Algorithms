n = int(input())
order = list(map(list, input().split()))
start = list(map(list, input().split()))

if start and n == len(start[0]):
  print(''.join(map(str, start[0])))
else:
  preference = {}
  for i in range(len(order[0])):
    preference[order[0][i]] = i
  brackets = {'(': ')', '[': ']'}
  stack = []
  if start:
    for i in start[0]:
      if stack and brackets[stack[-1]] != i:
        stack.append(i)
        next
      elif stack and brackets[stack[-1]] == i:
        stack.pop()
        next
      else:
        stack.append(i)
  opening = order[0][min(preference['('], preference['['])]
  if not start:
    stack.append(opening)
    start.append(list(opening))
  if not stack:
    stack.append(opening)
    start[0].append(opening)
  while len(stack) < n - len(start[0]):
    top = stack[-1]
    closing = brackets[top]
    if preference[closing] > preference[opening]:
      stack.append(opening)
      start[0].append(opening)
    else:
      stack.pop()
      start[0].append(closing)
      if not stack:
        stack.append(opening)
        start[0].append(opening)

  while stack:
    top = stack[-1]
    start[0].append(brackets[top])
    stack.pop()
  print(''.join(map(str, start[0])))
