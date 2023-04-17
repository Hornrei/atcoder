n = input()

if (n.find('B') % 2 == 0 and n.rfind('B') % 2 == 1) or (n.find('B') % 2 == 1 and n.find('B') % 2 == 0):
    s = True
else:
    s = False

if n.find('R') < n.find('K') < n.rfind('R'):
    s1 = True
else:
    s1 = False
    
if s and s1:
    print('Yes')
else:
    print('No')