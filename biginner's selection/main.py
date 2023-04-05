# s = list(input())

# s.reverse()

# #"a" in s

# if "a" in s:
#     t = len(s) - s.index("a")
#     print(t)
# else:
#     print(-1)


# arr = [0, 1, 2]

# print(list(itertools.permutations(arr)))

# import itertools
# n = int(input())
# p = list(map(int, input().split()))

# i = 1
# a = []
# while i <= n:
#     a.append(i)
#     i += 1

# b = list(itertools.permutations(a))
# e = []
# for i in b:
#     e.append(list(i))


# f = (e[(e.index(p)) - 1])

# print(*f, end="")

n = int(input())
s = list(map(int, input().split()))

for i in range(len(s)-1, 0, -1):
    if s[i] - s[i-1] < 0:
        f = i
        break

ans = s[:f-1]
t = s[f-1:]
k = s[f-1]

key = -1
for i in range(len(t)):
    if t[i] > key and k > t[i]:
        key = t[i]

ans.append(key)
t.remove(key)
t.sort(reverse=True)
ans.extend(t)

print(*ans, end='')