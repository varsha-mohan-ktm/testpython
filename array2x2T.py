x=int(input("Enter the no.of elements in array"))
l=list()
m=list()
s=list()
for i in range(x):
    l.append(int(input("Enter the elements of first array")))
for i in range(x):
    m.append(int(input("Enter the elements of second array")))
s.append(l)
s.append(m)
print("\nthe matrix is : ")
for i in range(x):
    for j in range(x):
        print(s[i][j],end=' ')
    print()
print("\nthe transpose is : ")
for i in range(x):
    for j in range(x):
        print(s[j][i],end=' ')
    print()