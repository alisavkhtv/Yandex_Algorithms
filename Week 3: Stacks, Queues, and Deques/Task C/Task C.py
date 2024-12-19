n, window = map(int, input().split())
nums = list(map(int, input().split()))
answer = []
stack_wind = []
for i in range(len(nums)):
  if not stack_wind:
    next
  else:
    if stack_wind[0] == i - window:
      stack_wind.pop(0)
  if not stack_wind:
    next
  else:
    while stack_wind and nums[i] <= nums[stack_wind[-1]]:
      stack_wind.pop()
  stack_wind.append(i)
  if i + 1 >= window:
    answer.append(nums[stack_wind[0]])
print(*answer, sep = '\n')
