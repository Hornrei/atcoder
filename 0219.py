# n, m = map(int, input().split())
# li = list(map(int, input().split()))
# ls = list(map(int, input().split()))
# a = 0
# for i in ls:
#     a += li[i - 1]

# print(a)


# n, k = map(int, input().split())
# li = list(input())
# ls = []
# cou = 0

# for i in range(len(li)):
#     if cou < k:
#         if li[i] == 'o':
#             cou += 1
#     else:
#         li[i] = 'x'

# for i in li:
#     print(i,end='')

n, k = map(int, input().split())
li = list(map(int,input().split()))
a =[]

for i in range(k):
    if i not in li:
        a.append(i)
if a == []:
    print(k)
else:
    print(max(a) + 1)
