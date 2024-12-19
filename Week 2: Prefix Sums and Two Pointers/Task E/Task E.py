n = int(input())
nums = list(map(int, input().split()))
sort = sorted(nums)
answer = []
while n > 0:
  if n%2 != 0:
    answer.append(sort[n//2])
    sort.pop(n//2)
  else:
    answer.append(sort[n//2-1])
    sort.pop(n//2 - 1)
  n -= 1
print(" ".join(map(str, answer)))
