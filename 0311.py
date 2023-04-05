# s = list(input())
# a = 0

# while a <= len(s) - 1:
#     b = s[a]
#     s[a] = s[a + 1]
#     s[a + 1] = b
#     a += 2

# for i in s:
#     print(i,end="")

n = int(input())
a = list(map(int, input().split()))
cou = 0
b = []
c = []

for i in range(1,n + 1):
    if i not in a:
        c.append(i)
cou = len(c)

# print(c)
for i in range(1,n):
    if a[i - 1] not in c:  
        if i in b:
            cou += 1
            c.append(a[i - 1])
        else:
            b.append(a[i - 1])


print(cou)
for i in sorted(c):
    print(i,end=" ")


