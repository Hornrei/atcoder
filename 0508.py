# n, a, b = map(int,input().split())

# l = list(map(int, input().split()))




h, w = map(int, input().split())



l = [list(input().split()) for i in range(h)]
kekka = ""
for i in range(w):
    cou = 0
    for j in range(h):
        if l[i][j] == "#":
            cou += 1
    kekka += f"{cou} "
    