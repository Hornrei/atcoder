# n = int(input())

# while n >= 0:
#     print(n)
#     n -= 1



# s = list(input())
# hantei = True

# def isint(j):
#     try:
#         int(j)
#     except:
#        return False
#     else:
#         return True

# if len(s) == 8:
#     if s[0].isalpha():
#         for i in range(1,6):
#             if isint(s[i]):
#                 if s[1] != "0":
#                     pass    
#                 else:
#                     hantei = False
#                     break
#             else:
#                 hantei = False
#                 break
#     else:
#         hantei = False

#     if s[7].isalpha():
#         pass
#     else:
#         hantei = False
# else:
#     hantei = False                


# if hantei:
#     print("Yes")
# else:
#     print("No")



3
# n, t = map(int, input().split())
# l = list(map(int, input().split()))


# b = 0
# for i in l:
#     b += i

# c = t % b

# d = 0
# e = 0
# sa = 0
# for j in range(n):
#     if l[j] + d < c:
#         d += l[j]
#     else:
#         kekka =   e += l[i]
#         sa = c - e
#         break

# print(kekka,sa#添削ver.
j + 1
#         for i in range(0,j):
#           
)



n, t = map(int, input().split())
l = list(map(int, input().split()))

# 違う書き方

b = sum(l)  

c = t % b   

d = 0   
e = 0
sa = 0
for j in range(n):
    if l[j] + d < c:
        d += l[j]
    else:
        kekka = j + 1
        
        # # これ実はいらない
        # for i in range(0,j):
        #     e += l[i]
        sa = c - d
        break

print(kekka,sa)








    