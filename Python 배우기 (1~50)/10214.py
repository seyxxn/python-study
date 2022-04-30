t = int(input())
for i in range(t):
    yon = 0
    ko = 0
    for j in range(9):
        y, k = map(int, input().split())
        yon += y
        ko += k
    if (yon > ko):
        print("Yonsei")
    elif ( yon < ko ):
        print("Korea")
    elif (yon == ko):
        print("Draw")