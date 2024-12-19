my_line = str(input().split())
stack = []
all_brackets = {'(': ')', '[': ']', '{': '}'}

def check_sequence(sequence):
  for i in sequence:
    if i in all_brackets:
      stack.append(i)
    elif i in all_brackets.values():
      if not stack:
        return 'no'
      else:
        top = stack.pop()
        if all_brackets[top] != i:
          return 'no'
  if not stack:
    return 'yes'
  else:
    return 'no'

print(check_sequence(my_line))
