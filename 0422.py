# n = int(input())
# s = input()

# if s.find("|") < s.find("*") < s.rfind("|"):
#     print("in")
# else:
#     print("out")


#n人プレイヤー　数が番号　i
#iが出したカード　色C　値　R
# n, t = map(int,input().split())

# c = list(map(int,input().split()))
# r = list(map(int,input().split()))

# a = []
# ans = 0

# if t in c:
#     for i in range(len(c)):
#         if c[i] == t:
#             a.append(r[i])
#     ans = r.index(max(a))
# else:
#     for j in range(len(c)):
#         if c[0] == c[j]:
#             a.append(r[j])
#     ans = r.index(max(a))

# print(ans + 1)


n = int(input())
s = list(input())

ans = 0
cou = 0
flg = False
a = []

if "-" not in s:
    print(-1)
    exit()

if 'o' not in s:
    print(-1)
    exit()

for i in s:
    if i == "o":
        ans += 1
        flg = True
    else:
        flg = False
        a.append(ans)
        ans = 0
    
if flg:
    a.append(ans)
    
if a == [0]:
    print(-1)
else:
    print(max(a))