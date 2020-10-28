import copy

def check(arr, b):
    total = 0
    cnt = 0
    for i in range(len(arr)-1, -1, -1):
        total += int(arr[i]) * (b ** cnt)
        cnt += 1
    return total


for tc in range(1, int(input())+1):
    arr2 = list(input())
    arr3 = list(input())

    jin2 = arr2[::]
    jin3 = arr3[::]
    result2 = []

    for i in range(len(jin2)):
        if jin2[i] == '0':
            jin2[i] = '1'
            result2.append(''.join(jin2))
            jin2[i] = '0'
        elif jin2[i] == '1':
            jin2[i] = '0'
            result2.append(''.join(jin2))
            jin2[i] = '1'

    result3 = []
    for j in range(len(jin3)):
        if jin3[j] == '0':
            jin3[j] = '1'
            result3.append(''.join(jin3))
            jin3[j] = '0'
            jin3[j] = '2'
            result3.append(''.join(jin3))
            jin3[j] = '0'
        elif jin3[j] == '1':
            jin3[j] = '0'
            result3.append(''.join(jin3))
            jin3[j] = '1'
            jin3[j] = '2'
            result3.append(''.join(jin3))
            jin3[j] = '1'
        else:
            jin3[j] = '0'
            result3.append(''.join(jin3))
            jin3[j] = '2'
            jin3[j] = '1'
            result3.append(''.join(jin3))
            jin3[j] = '2'

    for i in result2:
        a = check(i, 2)
        for j in result3:
            b = check(j, 3)
            if a == b:
                print('#{0} {1}'.format(tc, a))


    # 2진수에서 다를 경우 하나씩
    # 3진수에서 다를 경우 하나씩
    # 모든 경우를 비교해야함.

'''      
1
1010
212
'''
