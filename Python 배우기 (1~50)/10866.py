n = int(input())
yes = 0
no = 0

for i in range(n):
    cute = int(input())
    if cute == 0 :
        no += 1
    elif cute == 1 :
        yes += 1

if yes > no :
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")