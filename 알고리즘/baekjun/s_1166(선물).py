import sys

N, L, W, H = map(int, sys.stdin.readline().split())

start = 0
end = max(L, max(W, H))

for i in range(10000):
    mid = (start + end) / 2
    f = (L//mid) * (W//mid) * (H//mid)
    if f >= N:
        start = mid
    else:
        end = mid


print('%.10f'% start)

'''
1 1 1 8
'''
