n = int(input())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
pointers = list(map(int, input().split()))

sorted_int = sorted(enumerate(nums1), key=lambda x: (x[1], nums2[x[0]]), reverse=True)
sorted_utl = sorted(enumerate(nums2), key=lambda x: (x[1], nums1[x[0]]), reverse=True)

unique_indices = []
unique_indices_set = set()

point_1 = 0
point_2 = 0

for i in range(len(pointers)):
  if pointers[i] == 0:
    while point_1 < len(sorted_int):
      index_1, val_1 = sorted_int[point_1]
      if index_1 not in unique_indices_set:
        unique_indices_set.add(index_1)
        unique_indices.append(index_1)
        point_1 += 1
        break
      point_1 += 1
  else:
    while point_2 < len(sorted_utl):
      index_2, val_2 = sorted_utl[point_2]
      if index_2 not in unique_indices_set:
        unique_indices_set.add(index_2)
        unique_indices.append(index_2)
        point_2 += 1
        break
      point_2 += 1

print(' '.join(map(str, list(map(lambda x: x + 1, unique_indices)))))
