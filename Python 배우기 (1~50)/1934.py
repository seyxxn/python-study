# 유클리드 호제법 사용
# 최대공약수
def gcd(x,y):
    while(y):
        x,y = y, x%y
    return x
# 최소공배수
def lcm(x,y):
    res = (x*y)//gcd(x,y)
    return res

t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    print(lcm(a,b))