import sys
import collections
sys.stdin = open('input5.txt', 'r')


def bfs():
    q = collections.deque()
    q.append([0, 0])
    arr[0][0] = 0   # 시작점 복구
    while q:
        i, j = q.popleft()
        for dx, dy in ([-1, 0], [1, 0], [0, -1], [0, 1]):
            nx, ny = dx+i, dy+j
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] > arr[i][j] + matrix[nx][ny]:    # 모든 경로를 다 지나가면서 최소값을 찾을수도 있음. 왔던 경로는 다시 안갈수도 있고
                    arr[nx][ny] = arr[i][j] + matrix[nx][ny]
                    q.append([nx, ny])


for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().rstrip())) for _ in range(N)]
    arr = [[1000000000000] * N for _ in range(N)]
    bfs()
    print(f'#{tc} {arr[N-1][N-1]}')