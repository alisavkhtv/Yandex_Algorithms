n = int(input())
pairs = []
for i in range(n-1):
  pairs.append(list(input().split()))

tree = {}
sons = set()
answer = {}

for s, f in pairs:
  if f not in tree:
    tree[f] = []
  tree[f].append(s)
  sons.add(s)

for f in tree.keys():
  if f not in sons:
    root = f
    break

def find_depth(element, current_depth):
  answer[element] = current_depth
  for s in tree.get(element, []):
    find_depth(s, current_depth+1)

find_depth(root, 0)
for i, j in sorted(answer.items()):
  print(i, j)
