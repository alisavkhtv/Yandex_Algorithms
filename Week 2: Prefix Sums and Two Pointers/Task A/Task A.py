n = int(input())
nums = list(map(int, input().split()))
prefixes = [0]*(len(nums) + 1)
for i in range(1, len(nums) + 1):
	prefixes[i] = nums[i-1] + prefixes[i-1]
print(" ".join(map(str, prefixes[1:])))
