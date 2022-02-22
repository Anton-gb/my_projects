# import math
#
#
# def num_round(num):
#     num += 0.5
#     return int(num)
#
#
# a = [1.2, 2.5, 3.5]
# b = []
# c = []
# for i in a:
#     g = num_round(i)
#     b.append(str(g))
#
# for i in a:
#     c.append(int(i))
#
# print(b)
# print(c)


a = [1, 2, 5, 10]
b = [0, 9, 8]

c = zip(a, b)
for i in c:
    print(i)
