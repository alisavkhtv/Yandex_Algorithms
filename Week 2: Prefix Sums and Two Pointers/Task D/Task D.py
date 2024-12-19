n, similar = map(int, input().split())
nums = list(map(int, input().split()))
sort = sorted(nums)
windows = []
lower = 0
higher = 0
for lower in range(n):
  while higher < n and (sort[higher] - sort[lower] <= similar):
    higher += 1
  windows.append(higher - lower)
print(max(windows))
