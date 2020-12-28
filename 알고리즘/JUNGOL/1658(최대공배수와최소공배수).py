def check(x, y):
    for i in range(1, x+1):
        if x % i == 0 and y % i == 0:
            ans = i

    return ans

n, k = map(int, input().split())

gcd = check(n, k) # 최대공약수
lcm = (n*k)//gcd # 최소공배수
# a * b = gcd * lcm

print(gcd)
print(lcm)