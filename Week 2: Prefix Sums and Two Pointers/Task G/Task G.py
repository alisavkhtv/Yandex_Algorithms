n, rude = map(int, input().split())
text = list(*input().split())
count_a = 0
count_b = 0
current_rude = 0
lower = 0
higher = 0
max_len = 0
while higher < n:
  if current_rude <= rude:
    if text[higher] == 'a':
      count_a += 1
    elif count_a == 0 and text[higher] == 'b':
      count_b += 1
    elif count_a != 0 and text[higher] == 'b':
      count_b += 1
      current_rude += count_a
    higher += 1

  if current_rude > rude:
    if text[lower] == 'a':
      count_a -= 1
      current_rude -= count_b
    elif text[lower] == 'b':
      count_b -= 1
    lower += 1

  if higher - lower > max_len:
      max_len = higher - lower

print(max_len)
