# Even or Odd
num=int(input("Enter a number: "))
if num%2==0:
    print("Even number")
else:
    print("Odd number")

# Positive, Negative or Zero
num=int(input("Enter a number: "))
if num==0:
    print("Zero")
elif num>0:
    print("Positive number")
else:
    print("Negative number")

# Find the Largest of Three Numbers
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if num1>num2 and num1>num3:
    print("Greatest no: ",num1)
elif num2>num3:
    print("Greatest no: ",num2)
else:
    print("Greatest no: ",num3)