num_chairs, target = list(map(int, input().split()))
height = list(map(int, input().split()))
weight = list(map(int, input().split()))

both = list(zip(height, weight))
sorted_both = sorted(both, key=lambda x: x[0])
sorted_height, sorted_weight = zip(*sorted_both)
sorted_height = list(sorted_height)
sorted_weight = list(sorted_weight)

lower = 0
higher = 0
weights = 0
queue = []
final = []
while higher < num_chairs:

  if sorted_weight[higher] >= target:
    final.append(0)
    break

  weights += sorted_weight[higher]
  if higher > 0:
    current_h = sorted_height[higher] - sorted_height[higher-1]
    while queue and queue[-1] < current_h:
      queue.pop()
    queue.append(current_h)

  while weights >= target:
    if queue:
      final.append(queue[0])
    weights -= sorted_weight[lower]
    lower += 1

    if lower <= higher:
      goodbye = sorted_height[lower] - sorted_height[lower-1]
      if queue and goodbye == queue[0]:
        queue.pop(0)

  higher += 1

print(min(final))
