import sys
sys.setrecursionlimit(100000)

def dfs(node):
    global min_c
    visited.append(node)
    if len(visited)==n: # 마지막 노드에서 처음으로 돌아가는 노드를 더해주기위해
        if cities_c[node][start_node] !=0:
            min_c.append(cities_c[node][start_node])
            result.append(sum(min_c))
            min_c.pop()
            return

    for w in range(n):
        if node!=w and not w in visited and cities_c[node][w] != 0:
            min_c.append(cities_c[node][w])
            dfs(w)
            visited.pop()
            min_c.pop()

n=int(input())
cities_c=[list(map(int,input().split())) for _ in range(n)]
result=[]
for i in range(n):
    visited=[]
    min_c=[]
    start_node=i
    dfs(i)
print(min(result))


'''
9
0 10 15 20 1 1 1 1 1
5 0 9 10 1 1 1 1 1
6 13 0 12 1 1 1 1 1
8 8 9 0 1 1 1 1 1
8 8 9 1 0 1 1 1 1
8 8 9 0 1 0 1 1 1
8 8 9 0 1 1 0 1 1
8 8 9 3 1 1 1 0 1
8 8 9 4 1 1 1 1 0

28
'''