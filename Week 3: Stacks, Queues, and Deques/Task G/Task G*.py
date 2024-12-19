n, limit = list(map(int, input().split()))
nums = list(map(int, input().split()))
time = 0
people = 0
for i in nums:
  people += i
  time += people
  if people <= limit:
    people = 0
  else:
    people -= limit
time += people
print(time)
