# a, b = map(int, input().split())
# ans = a
# for i in range(b - 1):
#     ans = a * ans

# print(ans)

n = int(input())
li = list(map(int, input().split()))
# print(li)
q = int(input())
print(q)

for _ in range(q):
    li1 = list(map(int, input().split()))
    if li1[0] == 1:
        li[li1[1] - 1] = li1[2]
    else:
        print(li[li1[1] - 1])




    



