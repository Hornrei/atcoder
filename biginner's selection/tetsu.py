# https://atcoder.jp/contests/abc245/tasks/abc245_b



# n = int(input())
# l = list(map(int, input().split()))

# a = 0
# hantei = True
# while hantei:
#     if a in l:
#         a += 1
#     else:
#         hantei = False
#         print(a)


# n = int(input())
# li = []
# for _ in range(n):
#     li.append(input())

# dic = {}
# for t in li:
#     if not t in dic:
#         print(t)
#         dic[t] = 0
#         continue






# https://atcoder.jp/contests/abc278/tasks/abc278_c

# from collections import defaultdict
# n, q = map(int, input().split())
# dic = defaultdict(int)

# for _ in range(q):
#     t, a, b = map(int, input().split())
#     if t == 1 and dic[a,b] == 0:
#             dic[a,b] += 1
#     elif t == 2 and dic[a,b] == 1:
#             dic[a,b] -= 1
#     elif not(dic[a,b] == 1 and dic[b,a] == 1):
#         print("No")
#     elif dic[a,b] == 1 and dic[b,a] == 1:
#             print("Yes")
    
        
         
        



# from collections import defaultdict

# n = int(input())

# dic = defaultdict(int)
# for _ in range(n):
#     s = input()
#     if dic[s] == 0:
#         print(s)
#     else:
#         print(f"{s}({dic[s]})")
#     dic[s] += 1



from collections import defaultdict
n, q = map(int, input().split())
dic = defaultdict(bool)

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if not dic[a,b]:
            dic[a,b] = True
    elif t == 2:
        if dic[a,b]:
            dic[a,b] = False
    else:
        if dic[a,b] and dic[b,a]:
            print("Yes")
        else:
            print("No")













