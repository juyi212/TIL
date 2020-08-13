#
# def re(words):
#     r_word = ''
#     for word in words[::-1]:
#         r_word+=word
#     return r_word

n=int(input())
for _ in range(n):
    words=input()
    if words == words[::-1]:
        print('0')
    else:
        for i in list(re_word[0:(len(re_word)//2)+1]):
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




