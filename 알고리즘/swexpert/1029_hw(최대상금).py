import sys
from itertools import combinations

sys.stdin = open('input10.txt', 'r')


# def check(cnt):
#     global ans
#
#     if not int(''.join(number)) in value:
#         value.add(int(''.join(number)))
#
#     if cnt == 0:
#         return
#
#     else:
#         for i in range(len(number)):
#             for j in range(i, len(number)):
#                 number[i], number[j] = number[j], number[i]
#                 if int(''.join(number)) in value:
#                     continue
#                 check(cnt-1)
#                 number[i], number[j] = number[j], number[i]



for tc in range(1, int(input())+1):
    number, k = input().split()
    number = list(number)
    ans = -123456
    value = set()
    while True:
        for i in range(len(number)):
            for j in range(i, len(number)):
                number[i], number[j] = number[j], number[i]
                if int(''.join(number)) in value:
                    value.add(int(''.join(number)))
                number[i], number[j] = number[j], number[i]

    # check(int(k))
    # print('#{} {}'.format(tc, max(value)))

