def roll(idx, clock):
    if clock == 1:
        tmp = mag[idx].pop()
        mag[idx].insert(0, tmp)

    elif clock == -1:
        tmp = mag[idx].pop(0)
        mag[idx].append(tmp)


def check(idx, clock, dir):
    if idx < 0 and idx >= 4:
        return
    if dir == 3:
        #   왼
        check(idx-1, -clock, 1)
        #   오
        check(idx+1, -clock, 2)

        roll(idx, clock)
    elif dir == 1:
        if mag[idx][2] != mag[idx +1][6]:
            check(idx-1, -clock, 1)
            roll(idx, clock)

    elif dir == 2:
        if mag[idx][6] != mag[idx-1][2]:
            check(idx+1, -clock, 2)
            roll(idx, clock)


for tc in range(1, int(input())+1):
    N = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]

    for i in range(N):
        idx, clock = map(int, input().split())

        check(idx-1, clock, 3)
