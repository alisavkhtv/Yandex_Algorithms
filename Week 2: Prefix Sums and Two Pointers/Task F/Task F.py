n = int(input())
nums = list(map(int, input().split()))

sort = sorted(nums)
prefixes1 = [0]*(n-1)
help1 = [0]*(n-1)
prefixes2 = [0]*(n)
help2 = [0]*(n-2)

for i in range(1, n-1):
  prefixes1[i] = prefixes1[i-1] + sort[i-1]

for i in range(1, n-1):
  help1[i] = sort[i]*prefixes1[i]

for i in range(1, n):
  prefixes2[i] = prefixes2[i-1] + help1[i-1]
prefixes2 = prefixes2[2:]

for i in range(n-2):
  help2[i] = sort[i+2]*prefixes2[i]
print(sum(help2) % 1000000007)
