# from bisect import bisect_left

# n, l = map(int, input().split())
# k = int(input())
# li = list(map(int, input().split()))



# def inx(li, target):
#     index = bisect_left(li, target)
#     if index == 0:
#         return li[0]
#     if index == len(li):
#         return li[-1]
    
#     a = target - li[index - 1]
#     b = li[index] - target
#     if a <= b:
#         return li[index - 1]
#     else:
#         return li[index]

# for i in range(1,n-1):
#     target = l / n * i
#     print(inx(li,target))


# n = int(input())
# li = sorted(list(map(int, input().split())))
# ls = []

# for i in range(n,len(li) - n):
#     ls.append(li[i])

# print(float(sum(ls) / len(ls)))

# s = list(input())

# for i in s:
#     if i.isupper():
#         print(s.index(i) + 1)


n = int(input())
li = sorted(list(map(int, input().split())))
ls = []
for i in range(n,len(li) - n):
    ls.append(li[i])

print(float(sum(ls) / len(ls)))

