everything = list(map(str, input().split()))
stack = []
for i in everything:
  if i.isdigit():
    stack.append(int(i))
  if i == '+':
    first = stack[-2]
    second = stack[-1]
    answer = first + second
    stack.pop()
    stack.pop()
    stack.append(answer)
  if i == '-':
    first = stack[-2]
    second = stack[-1]
    answer = first - second
    stack.pop()
    stack.pop()
    stack.append(answer)
  if i == '*':
    first = stack[-2]
    second = stack[-1]
    answer = first * second
    stack.pop()
    stack.pop()
    stack.append(answer)
  if i == '/':
    first = stack[-2]
    second = stack[-1]
    answer = first / second
    stack.pop()
    stack.pop()
    stack.append(answer)
  if i == '%':
    first = stack[-2]
    second = stack[-1]
    answer = first % second
    stack.pop()
    stack.pop()
    stack.append(answer)
  if i == '//':
    first = stack[-2]
    second = stack[-1]
    answer = first // second
    stack.pop()
    stack.pop()
    stack.append(answer)
print(answer)
