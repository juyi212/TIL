def prim(adj, start):
    weight = [1000000] * (V + 1)
    mst = [0] * (V + 1)
    weight[start] = 0   # 초기화 필수
    result = 0

    for _ in range(V + 1):
        # 현재 갈 수 있는 경로 중 가장 가중치가 작은 경로를 선택
        min_w = 10000000
        min_v = 0

        for i in range(V + 1):
            if mst[i] == 0 and weight[i] < min_w:
                min_w = weight[i]
                min_v = i

        mst[min_v] = 1  # 체크체크
        result += min_w

        for i in range(V + 1):
            if 0 < adj[min_v][i] < weight[i] and not mst[i]:
                weight[i] = adj[min_v][i]

    return result


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w
        adj[e][s] = w

    print('#{} {}'.format(tc, prim(adj, 0)))

# kruskal 로 풀어보기


'''
3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

'''
