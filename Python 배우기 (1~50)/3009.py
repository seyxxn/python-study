x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

rectangle_x = [x1,x2,x3]
rectangle_y = [y1,y2,y3]

if rectangle_x[0] == rectangle_x[1]:
    print(rectangle_x[2],end=" ")
elif rectangle_x[0] == rectangle_x[2]:
    print(rectangle_x[1],end=" ")
else :
    print(rectangle_x[0],end=" ")

if rectangle_y[0] == rectangle_y[1]:
    print(rectangle_y[2])
elif rectangle_y[0] == rectangle_y[2]:
    print(rectangle_y[1])
else :
    print(rectangle_y[0])