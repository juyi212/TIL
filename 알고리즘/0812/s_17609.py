def aa(words):
    if words == words[::-1]:
        return True

n=int(input())
for test_case in range(n):
    words=list(input())
    if words == words[::-1]:
        print('0')
    else:
        b =len(words)
        i=0
        while i<=b//2:
            f=i
            l=b-i-1
            if words[f] != words[l]:
                v = words.pop(f)
                q=aa(words)
                words.insert(f, v)
                words.pop(l)
                p=aa(words)
                if q ==1 or p==1:
                    print('1')
                    break
                else:
                    print('2')
                    break
            i+=1

