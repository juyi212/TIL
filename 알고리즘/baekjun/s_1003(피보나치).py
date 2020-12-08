import sys

# def check(n):
#     global zero, one
#     if n == 0:
#         zero += 1
#         return 0
#     elif n == 1:
#         one += 1
#         return 1
#     else:
#         return check(n-1) + check(n-2)


def check(n):
    global zero, one
    if n in dic:
        if n == 0:
            zero += 1
        elif n == 1:
            one += 1
        return dic[n]
    else:
        if n == 0:
            zero += 1
        elif n == 1:
            one += 1
        dic[n] = check(n - 1) + check(n - 2)
        return dic[n]


for _ in range(int(sys.stdin.readline())):
    dic = {0: 0, 1: 1}
    n =  int(sys.stdin.readline())
    zero, one = 0, 0
    check(n)
    print(zero, end =' ')
    print(one)