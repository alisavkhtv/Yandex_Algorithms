with open('input.txt', 'r') as myfile:
  num_people = int(myfile.readline())
  pairs = {}
  for i in range(num_people - 1):
    son, father = myfile.readline().split()
    pairs[son] = father
  for line in myfile.readlines():
    first, second = line.split()
    path_to_root = set()
    while first in pairs:
      path_to_root.add(first)
      first = pairs[first]
    path_to_root.add(first)

    while second not in path_to_root:
      path_to_root.add(second)
      second = pairs[second]

    print(second)
