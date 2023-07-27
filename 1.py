# n = int(input('Введите трехзначное число: '))

# res = 0

# for i in range(3):
#     ost = n % 10
#     n //= 10
#     res += ost

# print(res)

# n = 6

# p = n // 6 
# k = p * 4 

# print(p,k,p)


# n = 123600

# first = n // 1000
# res1 = 0
# res2 = 0


# for i in range(3):
#     ost = n % 10
#     n //= 10
#     res1 += ost

# for i in range(3):
#     ost = first % 10
#     first //= 10
#     res2 += ost

# if res1 == res2:
#     print('yes')
# else:
#     print('no')



a = 3
b = 2
c = 4

if a % c == 0 or b % c == 0 or c % a == 0 or c % b == 0:
    print('yes')
else:
    print('no')