print("python workshop started:")
name = input("enter your name:") 
print("welcome,",name)
#arithmatic oprator
a = int(input("enter first number:"))
b = int(input("enter the second number:"))
print("addition:",a+b)
print("substraction",a-b)
print("multiplication",a*b)
print("division",a/b)
#find type of data
x=10
y=2.5
z="python with AI"

print(type(x)),(type(y)),(type(z))
num = int(input("enter a number:"))
#even or odd
if num%2==0:
    print("even")
else:
    print("odd")
    
    
import random 
secret=random.randint(2,100)
while True:
     guess = int(input("guess the number"))
     if guess==secret:
         print("True!")
         break
     else:
         if guess > secret:
             print("too high,guess again")
         elif guess<secret:
             print("to low,guess again")
             
def square(n):
    return n*n
             