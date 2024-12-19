n, r = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
higher = 0
for lower in range(n-1):
  if nums[lower] + r > nums[-1]:
    break
  while higher < n and (nums[higher] - nums[lower] <= r):
    higher += 1
  answer += n - higher
print(answer)
