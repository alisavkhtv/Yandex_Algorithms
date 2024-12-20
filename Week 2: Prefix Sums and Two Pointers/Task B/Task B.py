n, neededsum = map(int, input().split())
nums = list(map(int, input().split()))
prefixes = [0]*(len(nums) + 1)
for i in range(1, len(nums) + 1):
	prefixes[i] = nums[i-1] + prefixes[i-1]
answer = 0
lower = 0
higher = 1
while higher < len(prefixes):
  if prefixes[higher] - prefixes[lower] == neededsum:
    answer += 1
    lower += 1
    higher += 1
  elif prefixes[higher] - prefixes[lower] > neededsum:
    lower += 1
  else:
    higher += 1
print(answer)
