# n = int(input())
# s = list(input())

# for i in range(n):
#     for j in range(2):
#         print(s[i],end="")

# a = 0
# b = input()
# ls = (b.split())

# for i in range(len(ls)):
#     if ls[i] == "0":
#         continue
#     else:
#         a += (2 ** i)
# print(a)


from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
kekka = defaultdict()
for i in range(1,n + 1):
    cou = 0
    while cou < 2:  
        for j in range(len(a)):
            if a[j] == i:
                cou += 1
                if cou == 2:
                    kekka[i] = j + 1
                    break


dic2 = sorted(kekka.items(), key=lambda x:x[1])

for i in range(len(dic2)):
    print(dic2[i][0],end=" ")


