#Python program of a Simple Calculator
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("First select the operators from the given list")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
c=input("")
num1=int(input("Enter the First Number :" ))
num2=int(input("Enter the Second Number :" ))
if ( c == '1'):
    print("The value of", num1 ,"+", num2 ,"=", add(num1,num2))
elif ( c == '2'):
        print("The value of", num1 ,"-", num2 ,"=", subtract(num1,num2))
elif ( c == '3'):
    print("The value of", num1 ,"*", num2 ,"=", multiply(num1,num2))
elif ( c == '4'):
    print("The value of", num1 ,"/", num2 ,"=", divide(num1,num2))
else:
    print ("Enter a valid option")