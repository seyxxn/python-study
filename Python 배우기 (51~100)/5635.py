n = int(input())
student = []

for i in range(n):
    name, d, m, y = map(str, input().split())
    studentDic = {}    
    studentDic['name'] = name
    studentDic['day'] = int(d)
    studentDic['month'] = int(m)
    studentDic['year'] = int(y)
    student.append(studentDic)

print(student) 

