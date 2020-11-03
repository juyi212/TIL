def check(n1, n2, i):
    if i == 0:
        return n1 + n2
    elif i == 1:
        return n1 - n2
    elif i == 2:
        return n1 * n2
    elif i == 3:
        return int(n1/n2)


def dfs(idx, total):
    global max_p, min_p

    if idx >= len(numbers)-1:
        if total > max_p:
            max_p = total
        if total < min_p:
            min_p = total

    for i in range(len(cards)):
        if cards[i]:
            cards[i] -= 1
            a = check(total, numbers[idx+1], i)
            dfs(idx+1, a)
            cards[i] += 1


for tc in range(1, int(input())+1):
    N = int(input())
    cards = list(map(int, input().split()))     # + , -, * , /
    numbers = list(map(int, input().split()))
    min_p = 100000000000
    max_p = -98765435677
    # 숫자를 하나씩 더해주고 중간중간의 연산을 더해줄 것임.
    dfs(0, numbers[0])
    print(max_p-min_p)