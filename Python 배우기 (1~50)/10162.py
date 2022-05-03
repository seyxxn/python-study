total = int(input())
a_btn = 300 # 5분
b_btn = 60 # 1분
c_btn = 10 # 10초

a,b,c = 0,0,0

if (total % 10 != 0 or total < 10) :
    print(-1)
    exit()

while(total > 0):
    if (total >= 300):
        a = total // a_btn
        total = total - a * a_btn
    elif (total >= 60):
        b = total // b_btn
        total = total - b * b_btn
    elif (total >= 10):
        c = total // c_btn
        total = total - c * c_btn

print(a,b,c)
