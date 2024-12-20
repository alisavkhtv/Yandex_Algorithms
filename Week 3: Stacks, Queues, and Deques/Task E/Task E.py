whole_line = str(input())
good_line = ['0']
printed_false = False
good = True
was_digit = False
good_signs = ['*', '-', '+']
balance = 0

prev_char = ''
prev2_char = ''

for sign in whole_line:
  if sign.isdigit():
    if prev_char == ' ' and prev2_char.isdigit():
        good = False
        printed_false = True
        break
    good_line.append(sign)
    prev2_char = prev_char
    prev_char = sign
  elif sign in good_signs:
    if (prev_char in good_signs) or (prev_char == ' ' and prev2_char in good_signs) or (prev_char == '(') or (prev_char == ' ' and prev2_char == '(') or (prev_char == ' ' and prev2_char == ' '):
      good = False
      printed_false = True
      break
    good_line.append(sign)
    prev2_char = prev_char
    prev_char = sign
  elif sign in [' ', '(', ')']:
    if sign == '(':
      balance += 1
    elif sign == ')':
      balance -= 1
      if balance < 0:
        good = False
        printed_false = True
    good_line.append(sign)
    prev2_char = prev_char
    prev_char = sign
  else:
    good = False
    printed_false = True
    break

if balance != 0:
  good = False
  printed_false = True

postfix = []
stack = []
if good == False:
  print('WRONG')
  printed_false = True
else:
  i = 1
  while i < len(good_line):
    if i == 1 and good_line[i] == '-':
      postfix.append(good_line[0])
    elif good_line[i].isdigit():
      number = good_line[i]
      while i + 1 < len(good_line) and good_line[i + 1].isdigit():
        number += good_line[i + 1]
        i += 1
      postfix.append(number)
    elif good_line[i] == '*':
      while stack and stack[-1] == '*':
        postfix.append(stack.pop())
      stack.append('*')
    elif good_line[i] == '+':
      while stack and (stack[-1] in good_signs):
        postfix.append(stack.pop())
      stack.append('+')
    elif good_line[i] == '-':
      if good_line[i-1] == '(':
        postfix.append('0')
      while stack and (stack[-1] in good_signs):
        postfix.append(stack.pop())
      stack.append('-')
    elif good_line[i] == '(':
      stack.append('(')
    elif good_line[i] == ')':
      while stack and stack[-1] != '(':
        postfix.append(stack.pop())
      stack.pop()
    i += 1
  if stack:
    if stack[-1] in good_signs:
      while stack:
        postfix.append(stack.pop())
  elif good == False:
    print('WRONG')
    printed_false = True
  elif not stack and good == True:
    printed_false = False
  else:
    print('WRONG')
    printed_false = True

if not printed_false:
  for i in postfix:
    if i.isdigit():
      stack.append(int(i))
    elif i in ['+', '-', '*']:
      if len(stack) < 2:
        printed_false = True
        break
      second = stack.pop()
      first = stack.pop()
      if i == '+':
        stack.append(first + second)
      elif i == '-':
        stack.append(first - second)
      else:
        stack.append(first * second)

  if printed_false or len(stack) != 1:
	  print('WRONG')
  else:
  	print(stack[0])
