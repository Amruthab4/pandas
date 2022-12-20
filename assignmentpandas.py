import pandas as pd 
n=int(input("enter number n:"))
p=int(input("enter number p:"))
q=int(input("enter number q:"))
r=int(input("enter number r:"))
s=int(input("enter number s:"))
y=n**2,p**2,q**2,r**2,s**2
x=pd.Series(y)
print(x)