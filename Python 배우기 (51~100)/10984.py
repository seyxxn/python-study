t = int(input())

for i in range(t):
    n = int(input())
    c_lst = []
    g_lst = []
    for j in range(n):
        c,g = map(float, input().split())
        c_lst.append(c)
        g_lst.append(c*g)
    print(int(sum(c_lst)), end=" ")
    print(f"{sum(g_lst)/int(sum(c_lst)):.1f}")