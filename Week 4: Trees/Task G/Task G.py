num_birds, num_pairs, mod = list(map(int, input().split()))
graph = {}
degrees = {}
edges = []
n_nodes = set()
exiting = False

for i in range(num_pairs):
  a, b = map(int, input().split())
  if a not in graph:
    graph[a] = []
    degrees[a] = 0
  if b not in graph:
    graph[b] = []
    degrees[b] = 0
  graph[a].append(b)
  graph[b].append(a)
  degrees[a] += 1
  degrees[b] += 1
  edges.append([a,b])
  n_nodes.add(a)
  n_nodes.add(b)

for node in degrees:
  not_leaf_count = sum(1 for n in graph[node] if len(graph[n]) > 1)
  if not_leaf_count > 2:
    exiting = True

def dfs(node, visited, my_graph):
    help_stack = [node]
    component = []

    while help_stack:
        upper = help_stack.pop()
        if not visited[upper]:
            visited[upper] = True
            component.append(upper)

            for close in my_graph.get(upper, 0):
                if close != 0:
                  if not visited[close]:
                      help_stack.append(close)

    return component

def factorial(n, mod):
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result

visited = [False] * (num_birds + 1)
components = []

for i in graph.keys():
  if not visited[i]:
    comp = dfs(i, visited, graph)
    components.append(comp)

free_birds = num_birds - sum(len(comp) for comp in components)
answer = 1

def count_leaves_by_parent(my_graph, leaves, mod):
    parents = {}

    for leaf in leaves:
        if leaf in graph and len(my_graph[leaf]) == 1:
            p = my_graph[leaf][0]
            if p in parents:
                parents[p] += 1
            else:
                parents[p] = 1

    answerr = 1

    for count in parents.values():
        answerr = (answerr * factorial(count, mod)) % mod

    return answerr

def has_triangle(my_graph):
  for key in my_graph.keys():
    closers_u = list(my_graph[key])
    count_closers = len(closers_u)

    for i in range(count_closers):
      for j in range(i + 1, count_closers):
        first = closers_u[i]
        second = closers_u[j]

        if second in my_graph[first]:
          return True

  return False

if has_triangle(graph):
  answer = 0
elif exiting:
  answer = 0
else:
  for comp in components:

    count_all_edges = sum(len(graph[x]) for x in comp) // 2
    leaves = {x for x in comp if len(graph[x]) == 1}

    if not leaves or len(leaves) == 1:
       answer = 0
       break

    leaves_count = len(leaves) if len(comp) != 2 else 0

    internal_edges_count = count_all_edges - leaves_count
    green_nodes = count_leaves_by_parent(graph, leaves, mod)

    if internal_edges_count == 0:
       answer *= green_nodes
       answer %= mod
       answer *= 2
       answer %= mod

    elif len(comp) == 2:
       answer *= 2
       answer %= mod

    elif internal_edges_count != 0:
       answer *= green_nodes
       answer %= mod
       answer *= 4
       answer %= mod

if free_birds != 0:
  for i in range(free_birds):
     answer *= (num_birds - free_birds) + 2 + i
     answer %= mod

answer *= factorial(len(components), mod)

print(answer % mod)
