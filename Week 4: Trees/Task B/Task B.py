import sys
sys.setrecursionlimit(100000)

n = int(input())

pairs = []
for i in range(n-1):
  pairs.append(list(input().split()))

tree = {}
sons = set()
for s, f in pairs:
  if f not in tree:
    tree[f] = []
  tree[f].append(s)
  sons.add(s)

for f in tree.keys():
  if f not in sons:
    root = f
    break

total = {}

def total_ancestors(element):
  if tree.get(element, 0) == 0:
    total[element] = 0
    return 0

  else:
    ancestor_count = 0
    for i in tree[element]:
      rec = total_ancestors(i)
      ancestor_count += rec + 1
    total[element] = ancestor_count
    return ancestor_count

for k in tree.keys():
  if k not in total:
    total_ancestors(k)

for i, j in sorted(total.items()):
  print(i, j)
