# n = int(input())
# s = list(input())
# a = 0
# t = 0
# for i in s:
#     if i == "A":
#         a += 1
#         if a == n / 2:
#             print("A")
#             quit()
#     else:
#         t += 1
#         if t == n / 2:
#             print("T")
#             quit()

# if a > t:
#     print("A")
# else:
#     print("T")

n = int(input())

a = list(map(int,input().split()))

kekka = []

for i in range(n):
    try:    
        if abs(a[i + 1] - a[i]) > 1:
            kekka.append(a[i])
            for j in range(1,abs(a[i + 1] - a[i])):
                if a[i] < a[i + 1]:
                    kekka.append(a[i] + j)
                else:
                    kekka.append(a[i] - j)
        else:
            kekka.append(a[i])
    except:
        kekka.append(a[i])

for i in kekka:
    print(i,end=" ")

