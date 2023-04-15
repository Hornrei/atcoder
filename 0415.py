# n = int(input())
# s = list(input())

# if "x" in s:
#     print("No")
#     exit()

# for i in s:
#     if i == "o":
#         print("Yes")
#         exit()
# print("No")
from collections import defaultdict
n = int(input())
q = int(input())

li = []
lis = defaultdict()

for _ in range(n):
    li.append([])

for i in range(q):
    da = list(map(int, input().split()))
    if da[0] == 1:
        li[da[2]-1].append(da[1])
        if da[1] not in lis.keys():
            lis[da[1]] = li[da[2]-1]
        else:
            lis[da[1]].append((li[da[2]-1]))
        continue

    if da[0] == 2:
        for k in li[da[1] - 1]:
            print(k,end=" ")
        print()
        continue
    else:
        for l in lis[da[1]]:
            print(l,end=" ")
        print()
