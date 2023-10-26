t = []
x = int(input("enter the number of student :"))
y = int(input("enter the number of modules :"))
for i in range(x):
    t1 = []
    for j in range(y):
        print("enter the mark of the student number",i+1,"of the module number",j+1)
        a = float(input())
        t1.append(a)
    t.append(t1)
for i in range(x):
    m = 0
    for j in range(y):
        m += (t[i][j])/y
    print("the average of the student number",i+1,"is :",m)
for j in range(y):
    min = t[0][j]
    max = t[0][j]
    for i in range(x):
        if min > t[i][j]:
            min = t[i][j]
        if max < t[i][j]:
            max = t[i][j]
    print("the maximum mark in the modul number",j+1,"is",max)
    print("the minimum mark in the modul number",j+1,"is",min)


