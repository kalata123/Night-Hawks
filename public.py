a = input('vuvedi purvi private code --> ')
b = input('vuvedi vtori private code --> ')
a = int(a)
b = int(b)

g = 2 
p = 1000000007

A = pow(g,a,p)
B = pow(g,b,p)


A1 = pow(B,a,p)
B1 = pow(A,b,p)
print(A1)
print(B1)
