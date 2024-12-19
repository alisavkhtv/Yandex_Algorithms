n = int(input())
nums = list(map(int, input().split()))
lower = 0
higher = n-1
sum = 0
while lower != higher:
  if nums[lower] < nums[higher]:
    sum += nums[lower]
    nums[lower+1] += nums[lower]
    lower += 1
  else:
    sum += nums[higher]
    nums[higher-1] += nums[higher]
    higher -= 1
print(sum)
