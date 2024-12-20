import sys
sys.setrecursionlimit(300000)

num_people = int(input())
pointers = list(map(int, input().split()))

pointers.insert(0, 0)

for i in range(len(pointers)):
  pointers[i] = pointers[i] - 1

def construct_tree(where_parents):
  tree = {}
  for i in range(len(where_parents)):
    tree[i] = {'value': 0, 'fired': False, 'parent': where_parents[i], 'children': []}
  for son, father in enumerate(where_parents):
    if father != -1:
      tree[father]['children'].append(son)
  return tree

my_tree = construct_tree(pointers)

def money(tree, node):
    total_depth = 1
    total_sum = 0
    for child in tree[node]['children']:
        rec = money(tree, child)
        total_depth += rec[0]
        total_sum += rec[1]

    total_sum += total_depth
    my_tree[node]['value'] = total_sum
    return total_depth, total_sum

money(my_tree, 0)
print(' '.join(str(node['value']) for node in my_tree.values()))
