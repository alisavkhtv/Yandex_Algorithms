n = int(input())
main_roads = list(map(int, input().split()))

rovers = []
for i in range(n):
  new = list(map(int, input().split()))
  rovers.append(new)

rovers_sort = sorted(rovers, key = lambda x: x[1])

if max(main_roads) - min(main_roads) == 2:
  corner = False
else:
  corner = True

queue1 = []
queue2 = []
queue3 = []
queue4 = []
answer_times = []

if corner == False:
  i = 0
  time = rovers_sort[i][1]
  while i < n:
    while i < n and rovers_sort[i][1] == time:
        if rovers_sort[i][0] == 1:
          queue1.append(rovers_sort[i])
        elif rovers_sort[i][0] == 2:
          queue2.append(rovers_sort[i])
        elif rovers_sort[i][0] == 3:
          queue3.append(rovers_sort[i])
        elif rovers_sort[i][0] == 4:
          queue4.append(rovers_sort[i])
        i += 1

    main_road_queue_empty = True

    for road in main_roads:
      if road == 1 and queue1:
        main_road_queue_empty = False
      elif road == 2 and queue2:
        main_road_queue_empty = False
      elif road == 3 and queue3:
        main_road_queue_empty = False
      elif road == 4 and queue4:
        main_road_queue_empty = False

    if queue1 and ((1 in main_roads) or (main_road_queue_empty)):
      first = queue1.pop(0)
      first.append(time)
      answer_times.append(first)
    if queue2 and ((2 in main_roads) or (main_road_queue_empty)):
      first = queue2.pop(0)
      first.append(time)
      answer_times.append(first)
    if queue3 and ((3 in main_roads) or (main_road_queue_empty)):
      first = queue3.pop(0)
      first.append(time)
      answer_times.append(first)
    if queue4 and ((4 in main_roads) or (main_road_queue_empty)):
      first = queue4.pop(0)
      first.append(time)
      answer_times.append(first)

    time += 1

  while queue1 or queue2 or queue3 or queue4:
    if queue1:
      first = queue1.pop(0)
      first.append(time)
      answer_times.append(first)

    if queue2:
      first = queue2.pop(0)
      first.append(time)
      answer_times.append(first)

    if queue3:
      first = queue3.pop(0)
      first.append(time)
      answer_times.append(first)

    if queue4:
      first = queue4.pop(0)
      first.append(time)
      answer_times.append(first)

    time += 1

  index_to_time_map = {tuple(rov[:2]): rov[2] for rov in answer_times}

  for rover in rovers:
      time_value = index_to_time_map.get(tuple(rover[:2]), None)
      print(time_value)

elif corner == True:
  i = 0
  time = rovers_sort[i][1]
  while i < n:
    while i < n and rovers_sort[i][1] == time:
        if rovers_sort[i][0] == 1:
          queue1.append(rovers_sort[i])
        elif rovers_sort[i][0] == 2:
          queue2.append(rovers_sort[i])
        elif rovers_sort[i][0] == 3:
          queue3.append(rovers_sort[i])
        elif rovers_sort[i][0] == 4:
          queue4.append(rovers_sort[i])
        i += 1

    if (1 in main_roads and 2 in main_roads):
      if queue1:
        first = queue1.pop(0)
      elif queue2:
        first = queue2.pop(0)
      elif queue3:
        first = queue3.pop(0)
      elif queue4:
        first = queue4.pop(0)

    elif (2 in main_roads and 3 in main_roads):
      if queue2:
        first = queue2.pop(0)
      elif queue3:
        first = queue3.pop(0)
      elif queue4:
        first = queue4.pop(0)
      elif queue1:
        first = queue1.pop(0)

    elif (3 in main_roads and 4 in main_roads):
      if queue3:
        first = queue3.pop(0)
      elif queue4:
        first = queue4.pop(0)
      elif queue1:
        first = queue1.pop(0)
      elif queue2:
        first = queue2.pop(0)

    elif (1 in main_roads and 4 in main_roads):
      if queue4:
        first = queue4.pop(0)
      elif queue1:
        first = queue1.pop(0)
      elif queue2:
        first = queue2.pop(0)
      elif queue3:
        first = queue3.pop(0)
    first.append(time)
    answer_times.append(first)

    time += 1

  while queue1 or queue2 or queue3 or queue4:
    if (1 in main_roads and 2 in main_roads):
      if queue2:
        first = queue2.pop(0)
      elif queue3:
        first = queue3.pop(0)
      elif queue4:
        first = queue4.pop(0)

    elif (2 in main_roads and 3 in main_roads):
      if queue3:
        first = queue3.pop(0)
      elif queue4:
        first = queue4.pop(0)
      elif queue1:
        first = queue1.pop(0)

    if (3 in main_roads and 4 in main_roads):
      if queue4:
        first = queue4.pop(0)
      elif queue1:
        first = queue1.pop(0)
      elif queue2:
        first = queue2.pop(0)

    if (1 in main_roads and 4 in main_roads):
      if queue1:
        first = queue1.pop(0)
      elif queue2:
        first = queue2.pop(0)
      elif queue3:
        first = queue3.pop(0)

    first.append(time)
    answer_times.append(first)
    time += 1

  index_to_time_map = {tuple(rov[:2]): rov[2] for rov in answer_times}

  for rover in rovers:
      time_value = index_to_time_map.get(tuple(rover[:2]), None)
      print(time_value)
