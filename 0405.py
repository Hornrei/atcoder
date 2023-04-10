n = int(input())
l = input()

for i in range(n - 1):
    if l[i] == l[i + 1]:
        print("No")
        exit()
else:
    print("Yes")