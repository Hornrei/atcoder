h, w = map(int, input().split())
data = [list(input()) for _ in range(h)]

kekka = 0
for i in range(len(data)):
    for p in range(len(data[i])):
        hako = data[i][p]
        if hako == '#':
            kekka += 1

print(kekka)


# n = int(input())
# a = list(map(int, input().split()))

# kekka = []
# for i in range(len(a)):
#     if i == 0:
#         kekka.append(a[0])
#     else:
#         kekka.append(a[i] - a[i - 1])
    

# for a in kekka:
#     print(f"{a}", end=' ')


s = list(input())
t = list(input())

e = 0
kekka = -1
while e < len(s):
    if s[e] == t[e]:
        e += 1
    else:
        kekka = t[e]
        break
if kekka == -1:
    e = len(t) - 1

print(e + 1)