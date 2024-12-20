import sys
sys.setrecursionlimit(100000)


with open('input.txt', 'r') as myfile:
    n = int(myfile.readline().strip())
    pairs = [list(map(int, myfile.readline().strip().split())) for _ in range(n - 1)]

def graph(pairs):
  g = {}

  for first, second in pairs:
    if first not in g:
      g[first] = []
    if second not in g:
      g[second] = []

    g[first].append(second)
    g[second].append(first)

  return g

to_skip = set()
def build_tree(my_graph, current_node):
  tree = {}
  to_skip.add(current_node)
  for value in my_graph[current_node]:
    if value not in to_skip:
      tree[value] = build_tree(my_graph, value)

  return tree

my_tree = {1: build_tree(graph(pairs), 1)}
answer = {}

def get_answer(tree, current_node):
  count = 0
  if current_node in tree:
    for son in tree[current_node]:
      count += get_answer(tree[current_node], son) + 1

  answer[current_node] = count
  return count

m = get_answer(my_tree, 1)
sorted_values = [answer[key] + 1 for key in sorted(answer.keys())]
print(' '.join(map(str, sorted_values)))
