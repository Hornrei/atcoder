# n = int(input())
# s = []
# for _ in range(n):
#     s.append(input())

# for i in range(n - 1,  -1, -1):
#     print(s[i])



# t = int(input())

# for _ in range(t):
#     n = int(input())
#     s = list(map(int, input().split()))
#     cou = 0
#     for i in s:
#         if i % 2 == 1:
#             cou += 1
#     print(cou)



# import math


# # if 

# # def soin(s):
# #     a = []
    
# #     while s % 2 == 0:
# #         a.append(2)
# #         s //= 2
# #     f = 3
# #     while f * f <= s:
# #         if s % f == 0:
# #             a.append(f)
# #             s //= f
# #             if len(a) >= 3:
# #                 return a
# #         else:
# #             f += 2
# #     if n != 1:
# #         a.append(s)
# #     return a




# n = int(input())




# def soin(s):
#     arr = []
#     temp = s
#     for i in range(2, int(-(-s**0.5//1))+1):
#         if temp%i==0:
#             cnt=0
#             while temp%i==0:
#                 cnt+=1
#                 temp //= i
#             arr.append([i, cnt])
#         if len(arr) >= 3:
#             break

#     if temp!=1:
#         arr.append([temp, 1])

#     if arr==[]:
#         arr.append([s, 1])

#     return arr


# for _ in range(n):
#     s = int(input())
#     aa = soin(s)[0][1]
#     if aa == 2:
#         print(soin(s)[0][0],soin(s)[1][0])
#     else:
#         print(soin(s)[1][0],soin(s)[0][0])


t = int(input())    

n1 = 9 * (10 ** 18)
n2 = n1 ** 0.5
n3 = n2 ** 0.5
li = [i for i in range(n1 + 1)]
for i in li[3:]:
    if li[i] % 2 == 0:
        li[0]

for i in range(3,n2 + 1):
    if i > n3:
        break
    if li[i] != 0:
        for j in range(i, n2 + 1, 2):
            if i * j >= n2 + 1:
                break
            li[i * j] = 0

for _ in range(t):
    s = int(input())
    for k in li:
        if k != 0:
            if s / (k ** 2) in li and s % (k ** 2) == 0:
                print(k, s / (k ** 2))
    
