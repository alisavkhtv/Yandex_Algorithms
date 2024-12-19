n = int(input())
nums = list(map(int, input().split()))
stack = []
answer = [-1]*n
for i in range(n):
  while stack and nums[i] < stack[-1][1]:
    top_ind, top_val = stack.pop()
    answer[top_ind] = i
  stack.append((i, nums[i]))
print(' '.join(map(str, answer)))
