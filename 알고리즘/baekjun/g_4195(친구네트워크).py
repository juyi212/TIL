# 분리집합 문제

def find(x):
    if parents[x] == x:
        return x

    p = find(parents[x])
    parents[x] = p
    return p


def union(parents, person1, person2, cnt):
    a = find(person1)
    b = find(person2)

    if a != b:
        parents[b] = a
        cnt[a] += cnt[b]


for tc in range(1, int(input())+1):
    n = int(input())
    parents = {}
    cnt = {}
    for i in range(n):
        p1, p2 = input().split()
        if p1 not in parents:
            parents[p1] = p1
            cnt[p1] = 1
        if p2 not in parents:
            parents[p2] = p2
            cnt[p2] = 1
        union(parents, p1, p2, cnt)
        print(cnt[find(p1)])
