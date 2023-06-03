n = int(input())
d ={}
ls = []
for i in range(n):
    s, a=input().split()
    d[s] = int(a)
    ls.append(s)

o = ls.index(min(d, key=d.get))

for j in range(o,len(ls)):
    print(ls[j],end=" ")

if o == 0:
    quit()

for k in range(0,o):
    print(ls[k],end=" ")






# n = list(input())

# if len(n) < 4:
#     for j in n:
#         print(j,end="")
#     quit()

# for i in range(3,len(n)):
#     n[i] = 0

# for j in n:
#     print(j,end="")
