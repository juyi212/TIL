n=int(input())
value = []
while True:
    a = n % 3
    value.append(str(a))
    n = n // 3
    if n//3 ==0:
        a=n%3
        value.append(str(a))
        break
value=''.join(value)
decimal=0
for idx, val in enumerate(value[::-1]):
    decimal+=(3**idx)*int(val)
print(decimal)
