# n = int(input())
# for _ in range(n):
#     a, b = map(int, input().split())
#     print(a + b)

# n , m = map(int, input().split())
# li = []
# for _ in range(n):
#     li.append(input())
# lis = li[:m]

# for i in range(m):
#     print(sorted(lis)[i])

# n, m = map(int, input().split())
# li = []
# for _ in range(n):
#     li.append([])

# for _ in range(m):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     li[a].append(b)
#     li[b].append(a)
# print(li)


# n, m = map(int, input().split())

# p = [-1] * (n + 1)
# def root(x):
#     if p[x] < 0:
#         return
#     p[x] = root(p[x])
#     return p[x]

# def unite(x, y):
#     x = root(x)
#     y = root(y)
#     if x == y:
#         return
#     p[y] = x

# c = 0
# for _ in range(m):
#     a, b = map(int, input().split())
#     if root(a) == root(b):
#         c += 1

# print(f'結果{c}')
