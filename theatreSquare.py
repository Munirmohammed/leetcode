def teaterSquare(m,n,a):
    if m//a < m/a:
        side1=m//a+1
    else:
        side1=m/a
    if n//a < n/a:
        side2=n//a+1
    else:
        side2=n/a
    return int(side2*side1)
    
temp=input().split()
m=int(temp[0])
n=int(temp[1])
a=int(temp[2])
print(teaterSquare(m,n,a))
