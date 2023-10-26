t = []

for i in range(5):
    t1 = []
    for j in range(3):
        print("enter the mark of the student number",i+1,"of the module number",j+1)
        a = float(input())
        t1.append(a)
    t.append(t1)
for i in range(5) :
    m = 0
    for j in range(3):
        m += (t[i][j])/3
    print("the average of the student number",i+1,"is :",m)
for j in range(3):
    min = t[0][j]
    max = t[0][j]
    for i in range(5):
        if min > t[i][j]:
            min = t[i][j]
        if max < t[i][j]:
            max = t[i][j]
    print("the maximum mark in the modul number",j+1,"is",max)
    print("the minimum mark in the modul number",j+1,"is",min)


