n=int(input())

def re(words):
    r_word = ''
    for word in words[::-1]:
        r_word+=word
    return r_word

for test_case in range(n):
    words=input()
    re_word=re(words)
    if words == re_word:
        print('0')
    else:
        for i in list(re_word):
            new = list(re_word)
            new2=''
            new.remove(i)
            for j in new:
                new2+=j
            new3=re(new2)
            if new2 == new3:
                print('1')
                break
        else:
            print('2')





