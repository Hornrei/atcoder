# s = list(input())

# a = 0
# for i in s:
#     if i == "v":
#         a += 1
#     else:
#         a += 2

# print(a)

s = input()
t = input()

a = s.find(t)

if a == -1:
    ans = "No"
else:
    ans = "Yes"

print(ans)

