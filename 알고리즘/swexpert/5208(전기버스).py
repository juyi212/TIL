import sys
sys.stdin = open('input12.txt','r')

def dfs(idx, total, cnt):
    global min_ch

    if total < 0:
        return

    if idx >= N-1:
        if total >= 0:
            if min_ch > cnt:
                min_ch = cnt
                return
        return

    if min_ch > cnt:
        dfs(idx+1, total-1, cnt)
        dfs(idx+1, M[idx]-1, cnt+1)


for tc in range(1, int(input())+1):
    N, *M = map(int, input().split())
    min_ch = 100000
    dfs(0, M[0], 0)
    print('#{} {}'.format(tc, min_ch))

