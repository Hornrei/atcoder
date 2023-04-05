n = list(map(int, input().split()))
x = list(map(int, input().split()))



print(x.index((n[1])) + 1)












N = int(input())
l1 = []
for i in range(N):
    a,b=input()
    l1.append([a, b])

for j in l1:
    for h in j:
        # k=[]
        # k.append(h)
        if h == j[0]:
            if j[0] == "H" or j[0] == "D" or j[0] == "C" or j[0] == "S":
                kekka = "ok"
                    # or "D" or "C" or "S":
            else:
                kekka = "No"
               
        if h == "A" or h =="2" or h =="3" or h =="4" or h =="5" or h =="6" or h =="7" or h =="8" or h =="9" or h =="T" or h =="J" or h =="Q" or h =="K":
            kekka = "ok"
        else:
            kekka = "No"

if any(l1.count(k) > 1 for k in l1):
    kekka = "No"
else:
    kekka = "Yes"


if kekka == "No":
    kekka = "No"
else:
    kekka = "Yes"
print(kekka)


            
        





