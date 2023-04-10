# n, d = map(int,input().split())
# t = list(map(int,input().split()))

# for i in range(len(t) - 1):  
#         if t[i + 1] - t[i] <= d:
#             print(t[i + 1])
#             exit()
# print("-1")


# s = list(input())

# def index(li, num):
#     #liはリスト本体、numは探索したい文字
#     index_l = []
#     for i in range(0,len(li)):
#         if num == li[i]:
#             index_l.append(i)
        
#     return index_l

# kekka = index(s,'B')

# if (kekka[0] % 2 == 0 and kekka[1] % 2 == 1) or (kekka[0] % 2 == 1 and kekka[1] % 2 == 0):
#         flg = False
#         flg1 = False
#         for i in range(0,len(s) - 1):
#             if not flg and s[i] == "K":
#                 print("No")
#                 exit()
#             if not flg and s[i] == "R":
#                 flg = True
#                 continue
#             if flg and not flg1 and s[i] == "R":
#                 print("No")
#                 exit()
#             if flg and s[i] == "K":
#                 flg1 = True
#                 continue
#         print("Yes")
             
# else: 
#     print("No") 


# h, w = map(int, input().split())
# for i in range(h):
#     l = list(input())
#     cou = 3
#     kekka = []
#     pct = ["P","C","T"]
#     for j in l:
#         while j != ".":
#             kekka.append(pct[cou % 3])
#             cou += 1

a, b = map(int, input().split())

cou = 0

while a != b:
    if a < b:
        b = b - a
        cou += 1
        continue
    if b < a:
        a = a - b
        cou += 1
        continue
print (cou)  
        