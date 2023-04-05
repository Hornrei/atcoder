# a, b = map(int, input().split())

# if a == b / 2 or b == a * 2 + 1:
#     print("Yes")
# else:
#     print("No")



# n = int(input())
# s = list(input())

# for i in range(1, n):
#     cou = 0
#     # if cou == len(s) - 1:
#     #     print(cou)
#     #     break
#     try:
#         for j in range(len(s)):
#             if s[j] != s[j + i]:
#                 cou += 1
#             else:
#                 print(cou)
#                 break
#     except:
#         print(cou)


import string

s = input()
li = list(s)
lis = list(string.ascii_uppercase)

# if len(li) == 1:
#     print(lis.index(s) + 1)
#     quit()


# kekka = 0
# for i in range(len(li), -1, -1):
#     for j in range(len(li) - 1):
#         kekka += 26 ** i + (lis.index(li[j]) + 1) 
# print(kekka - 1)

kekka = 0
for i in range(len(li)):
    for j in reversed(li):
        a = lis.index(j) + 1
        kekka += 26 ** i * a
print(kekka)





