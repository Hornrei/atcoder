# s = list(input())
# a = []
# for i in s:
#     if i == '0':
#         a.append("1")
#     else:
#         a.append("0")

# for i in a:
#     print(i,end='')

# n, m = map(int, input().split())
# a = []
# if m == 0:
#     for i in range(1,n + 1):
#         print(i)
#     quit()

# for i in range(m):
#     a.append(int(input()))

# li = []
# for i in range(1,n + 1):
#     li.append(i)

# for i in a:
#     li.insert(i,-1)
# n, m= map(int, input().split())
# g = [[] for i in range(n)]
# li =[]
# lis = list(map(int, input().split()))
# for i in lis:
#     li.append(i - 1)
# for i in li:
#     g[i].append([i, i + 1])
#     # g[i + 1].append([i,i + 1])

# for i in g:
#     a = sorted(i)
#     print(a)

# n, m = map(int, input().split())
# g = [[] for _ in range(n)]
# a = list(map(int, input().split()))
# for i in a:
#     i -= 1
#     g[i].append(i + 1)
#     g[i + 1].append(i)

# print(g)


from itertools import combinations
r = 2
n, m = map(int, input().split())
li = [[] for _ in range(m)]
for i in range(m):
    c = int(input())
    s = {map(int, input().split())}
    li[i].append(s)


