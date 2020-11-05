def find_set(x):
    if x == parent[x]:
        return x

    p = find_set(parent[x])
    parent[x] = p
    return p


def union(x, y):
    a = find_set(x)
    b = find_set(y)
    if a != b:
        parent[b] = a



for tc in range(1, int(input())+1):
    N, M = map(int, input().split())    # N 명, M 쪽지 횟수
    parent = list(range(N+1))
    p = list(map(int, input().split()))
    for i in range(M):
        p1, p2 = p[i*2], p[i*2+1]
        union(p1, p2)   # 합치기

    result = []
    for i in range(N+1):
        result.append(find_set(parent[i]))  # 찾아 주기
    new = set(result)
    print('#{} {}'.format(tc, len(new)-1))





'''
1
7 4
2 3 4 5 4 6 7 4
'''
'''
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4

'''