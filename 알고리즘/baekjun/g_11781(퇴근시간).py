import sys

def check(weight):
    #   회사에서부터 end 까지의 시간을 찾아서 넣기
    weight[1] = 0
    U = {0} # 정점을 방문할 때마다, 정점을 추가
    while len(U) < N+1:
        min_w = INF
        min_idx = -1
        for i in range(1, N+1):
            if i not in U and weight[i] < min_w:
                min_w = weight[i]
                min_idx = i

        U.add(min_idx) # 방문

        for i in range(1, N+1):
            if i not in U:  # 방문하지 않았으면서
                # 방금 선택한 정점을 통하여 i 노드로 가는 비용이
                # 기존에 i로 가는 비용보다 더 싸다면, 업데이트
                tmp = min_w + matrix[min_idx][i]
                if traffic[min_idx][i]:
                    if matrix[min_idx][i] < E:
                        if tmp > S:
                            if min_w > S:
                                # 한 번 더 더해진 값들임
                                tmp += tmp - min_w
                            else:
                                tmp += tmp - S
                            if tmp > E:
                                # 2분에 -> 1 거리라서
                                tmp -= (tmp - E)/ 2

                if weight[i] > tmp:
                    weight[i] = tmp

    return weight   # 시작점으로부터 각 정점까지 최소비용이 저장된 배열 반환


N, M, S, E = map(int, sys.stdin.readline().split())
# N개 지점, M 간선, S, E 퇴근 시작 끝
INF = float('inf')
matrix= [[INF]*(N+1) for _ in range(N+1)]
traffic = [[False]*(N+1) for _ in range(N+1)]
for i in range(M):
    A, B, L, t1, t2 = map(int, sys.stdin.readline().split())
    # t1 A->B 막힘
    # t2 B->A 막힘
    if t1 == 1:
        traffic[A][B] = True
    if t2 == 1:
        traffic[B][A] = True
    matrix[A][B] = L
    matrix[B][A] = L

weight = [INF]*(N+1)
check(weight)
weight.sort()
print(weight[-2])

# 최소비용까지 구함
# 이어지는 구간
# 이어지지않는 구간
