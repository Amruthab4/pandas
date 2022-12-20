#2nd question
import pandas as pd 
n=int(input("enter number n:"))
p=int(input("enter number p:"))
q=int(input("enter number q:"))
r=int(input("enter number r:"))
s=int(input("enter number s:"))
y=n**2,p**2,q**2,r**2,s**2
x=pd.Series(y)
print(x)


#1st question
import pandas as pd 
n=pd.series([1,6,7,8,9,0,5])
n2=pd.series([3,5,6,7,9,8,2])
print(n)
print(n2)
y=n+n2
print(y)
y1=n-n2
print(y1)
y2=n*n2
print(y2)
y3=n/n2
print(y3)
y4=n%n2
print(y4)
print("addition:",y)
print("subtraction:",y1)
print("multiplication:",y2)
print("division:",y3)
print("mod:",y4)



import pandas as pd 
n=int(input("enter number n:"))
p=int(input("enter number p:"))
y=n+p,n-p,n*p,n/p,n%p
x=pd.Series(y)
print(x)