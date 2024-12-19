def insert(tree, value, depth = 0):
  if tree is None:
    print('DONE')
    return {'current_node': value, 'depth': depth, 'left': None, 'right': None}

  elif tree['current_node'] == value:
    print('ALREADY')

  elif tree['current_node'] > value:
    tree['left'] = insert(tree['left'], value, depth + 1)

  elif tree['current_node'] < value:
    tree['right'] = insert(tree['right'], value, depth + 1)

  return tree

def find(tree, value):
  if tree is None:
    print('NO')
    return None

  elif tree['current_node'] == value:
    print('YES')
    return tree

  elif value > tree['current_node']:
    return find(tree['right'], value)

  return find(tree['left'], value)

def print_tree(tree):
  if tree is not None:
    print_tree(tree['left'])
    print('.'*tree['depth'], tree['current_node'], sep = '')
    print_tree(tree['right'])

with open('input.txt', 'r') as newfile:
  tree = None
  for line in newfile.readlines():
    line = line.strip()
    if line == 'PRINTTREE':
      print_tree(tree)
      continue

    action, value = line.split()
    value = int(value)
    if action == 'ADD':
      tree = insert(tree, value)
    elif action == 'SEARCH':
      search = find(tree, value)
