n = int(input())

for _ in range(n):
    cou = 0
    t = int(input())
    li = list(input())
    if li.count('1') == 2 and (li[li.index("1") + 1] == '1' or li.index("1") - 1 == "1"):
        print(-1)

    elif li.count("1") % 2 == 1:
        print(-1)
        
    elif li.count("1") == 0:
        print(0)
        
    else:
        cou = li.count("1")
        print(int(cou / 2))
            




