







# x, k = map(int, input().split())

# xa = list(str(x))

# x1 = list(map(int, xa))

# if len(x1) < k:
#     print(0)
#     quit()

# for i in range(len(x1),len(x1) - k, -1):
#     try:
#         if x1[i - 1] >= 5 and x1[i - 1] <= 10 and i != 1:
#                 x1[i - 2] += 1
#         elif i == 1 and x1[i - 1] >= 10:
#             x1.insert(0,1)
#             break
#         x1[i - 1] = 0        
#     except:
#         x1.insert(0, 1)
# # print(x1)

# a = ""
# xb = list(map(str, x1))
# for i in xb:
#     a += i
# b = list(a) 

# if len(xa) + 1 < len(b):
#     for i in range(1, len(b)):
#         print(b[i],end="")
# else:
#     for i in b:
#          print(i,end="")    

    #x1...xを1桁ずつリストに入った形


# y = []
# for i in range(len(x1) - k - 1):
#     y.insert(0,x1[i])
# print(y)            #y => 変わらなかった値




# x, k = map(int, input().split())

# xa = list(str(x))
# x1 = list(map(int, xa)) 


# if len(x1) < k:
#     print(0)
#     quit()

# if len(x1) == 1:
#     if x >= 5:
#         print(10)
#     else:
#         print(0)
#     quit()

# for i in range(len(x1),len(x1) - k, -1):
#     i -= 1
#     if x1[i] >= 5 and i == 0:
#         x1[i] = 0
#         x1.insert(0, 1)
#         break
#     elif x1[i] >= 5:
#         x1[i - 1] += 1
#     x1[i] = 0

# for i in x1:
#     print(i,end="")



# x, k = map(int, input().split())

# xa = list(str(x))
# x1 = list(map(int, xa)) 


# if len(x1) < k:
#     print(0)
#     quit()

# if len(x1) == 1:
#     if x >= 5:
#         print(10)
#     else:
#         print(0)
#     quit()


# for i in range(len(x1),len(x1) - k, -1):
#     i -= 1
#     if x1[i] >= 5:  
#         if i == 0:
#              x1[i] = 0
#              x1.insert(0, 1)
#              break
#         x1[i - 1] += 1
#     x1[i] = 0

# for i in x1:
#     print(i,end="")






#☆#
# x, k = map(int, input().split())

# for i in range(k):
#     a = (x / 10 ** i) % 10 
#     if a >= 5:
#         x = x + (10 ** i * (10 - a))
#     else:
#         x = x - (10 ** i * a)   
    
# print(int(x))


n = int(input())
a = list(map(int, input().split()))


for i in a:
    li = []
    for j in a:
        if i < j:
            li.append(j)
    try:
        print(len(set(li)))
    except:
        print(0)