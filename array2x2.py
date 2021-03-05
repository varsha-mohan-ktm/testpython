x=int(input("Enter the no.of elements in array"))
l=list()
m=list()
s=list()
for i in range(x):
    l.append(input("Enter the elements of first row"))
for i in range(x):
    m.append(input("Enter the elements of second row"))
s.append(l)
s.append(m)
for i in range(x):
    for j in range(x):
        print(s[i][j],end=' ')
    print()