def irr(arr,i):
    arr.pop(i)
    str(arr)
    if arr == arr[::-1]:
        return True
n=int(input())
for _ in range(n):
    words=input()
    if words == words[::-1]:
        print('0')
    else:
        b =len(list(words))
        for i in range(b//2):
            a = list(words)
            f=i
            l=b-i-1
            if a[f] != a[l]:
                v=irr(a,f)
                s = irr(list(words),l)
                if v ==1 or s ==1 :
                    print('1')
                    break
        else:
            print('2')
            break




