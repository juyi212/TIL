def check(n):
    global max_l
    q=[]
    q.append((n,0))
    while q:
        n,length=q.pop(0)
        if length>max_l:
            max_l=length
        result.append([n,length])
        for i in matrix[n]:
            if not i in visited:
                q.append((i,length+1))
                visited.append(i)
    return result

for tc in range(1,11):
    N,S=map(int,input().split())
    nodes=list(map(int,input().split()))
    matrix=[[] for _ in range(101)]
    for i in range(0,N,2):
        s,e=nodes[i],nodes[i+1]
        matrix[s].append(e)
    visited=[]
    result=[]
    max_l=0
    max_v=0
    check(S)
    for i in range(len(result)):
        if result[i][1]==max_l:
            if max_v<result[i][0]:
                max_v=result[i][0]
    print(max_v)



'''
300 42
42 68 35 1 70 25 79 59 63 65 6 46 82 28 62 92 96 43 28 37 92 5 3 54 93 83 22 17 19 96 48 27 72 39 70 13 68 100 36 95 4 12 23 34 74 65 42 12 54 69 48 45 63 58 38 60 24 42 30 79 17 36 91 43 89 7 41 43 65 49 47 6 91 30 71 51 7 2 94 49 30 24 85 55 57 41 67 77 32 9 45 40 27 24 38 39 19 83 30 42 34 16 40 59 5 31 78 7 74 87 22 46 25 73 71 30 78 74 98 13 87 91 62 37 56 68 56 75 32 53 51 51 42 25 67 31 8 92 8 38 58 88 54 84 46 10 10 59 22 89 23 47 7 31 14 69 1 92 63 56 11 60 25 38 49 84 96 42 3 51 92 37 75 21 97 22 49 100 69 85 82 35 54 100 19 39 1 89 28 68 29 94 49 84 8 22 11 18 14 15 10 17 36 52 1 50 20 57 99 4 25 9 45 10 90 3 96 86 94 44 24 88 15 4 49 1 59 19 81 97 99 82 90 99 10 58 73 23 39 93 39 80 91 58 59 92 16 89 57 12 3 35 73 56 29 47 63 87 76 34 70 43 45 17 82 99 23 52 22 100 58 77 93 90 76 13 1 11 4 70 62 89 2 90 56 24 3 86 83 86 89 27 18 58 33 33 70 55 22 90 
'''