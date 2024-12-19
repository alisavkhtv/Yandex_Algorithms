n = int(input())
nums = list(map(int, input().split()))
m, k = map(int, input().split())
indices_m = list(map(int, input().split()))

current_k = k
break_higher = False
break_0 = False
higher = (n-1)
lower = (n-1)
answer = [-1]*n
handle_faster = 1
raise_alarm = False

for lower in range(n-1, 1, -1):
    if nums[lower] == nums[lower-1] and k == n:
        handle_faster += 1
if handle_faster == n:
    answer = [1]*n

else:
    lower = (n-1)
    for higher in range(n-1, 0, -1):
        if higher < n-1 and nums[higher] == nums[higher+1] and k != 0:
            current_k += 1
        while lower != 0:
            if nums[lower] < nums[lower-1]:
                break_higher = True
                raise_alarm = False
                break
            else:
                if nums[lower] == nums[lower-1]:
                    if current_k != 0:
                        current_k -= 1
                        lower -= 1
                    elif current_k == 0 and raise_alarm == False:
                        raise_alarm = True
                    elif current_k == 0 and raise_alarm == True:
                        break_0 = True
                        break
                elif nums[lower] > nums[lower-1]:
                    raise_alarm = False
                    lower -= 1

        if break_higher == True:
            answer[higher] = lower + 1
            if higher == lower:
                lower = higher - 1

        elif break_0 == True:
            answer[higher] = lower + 1
            raise_alarm = False
            if higher == lower:
                lower = higher - 1

        else:
            answer[higher] = lower + 1

    if lower == 0:
        answer[lower:higher] = [1]*(higher-lower)

result = [answer[index-1] for index in indices_m]
print(' '.join(map(str, result)))
