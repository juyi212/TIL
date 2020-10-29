
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())    # 컨테이너 수, 트럭 수
    W = list(map(int, input().split()))     # 화물의 무게
    T = list(map(int, input().split()))     # 트럭의 적재용량
    check = []
    result = 0
    for i in range(M):
        max_t = 0
        j = 0
        while j < len(W):
            if T[i] >= W[j]:
                if max_t < W[j]:
                    max_t = W[j]
                    j += 1
                else:
                    j += 1
            else:
                j += 1
        if max_t in W:
            W.remove(max_t)
            result += max_t
    print('#{} {}'.format(tc, result))

'''
1
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
'''