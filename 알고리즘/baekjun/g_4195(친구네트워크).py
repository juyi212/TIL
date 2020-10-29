def getParent(parents, x):
    if parents[x] == x:     # 자기자신
        return x
    p = getParent(parents, parents[x])
    parents[x] = p
    return p


def unionParent(parents, x1, x2, cnt):
    a = getParent(parents, x1)
    b = getParent(parents, x2)

    if a != b:
        parents[b] = a
        cnt[a] += cnt[b]


def findParent(x, parents):
    if parents[x] == x:
        return x
    return findParent(parents[x], parents)


for _ in range(1, int(input())+1):
    F = int(input())
    parents = {}
    cnt = {}
    for i in range(F):
        f1, f2 = input().split()
        if f1 not in parents:
            parents[f1] = f1
            cnt[f1] = 1
        if f2 not in parents:
            parents[f2] = f2
            cnt[f2] = 1
        unionParent(parents, f1, f2, cnt)
        print(cnt[findParent(f1, parents)])
