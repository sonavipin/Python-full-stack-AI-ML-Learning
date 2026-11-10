'''
    Task: Ask the user for:
        - Name
        - Age
        - Python mark
        - SQL mark
    Then calculate and display total and average.
'''
name=input("Enter your name: ")
age=int(input("Enter your age: "))
python_mark=int(input("Enter your python mark: "))
sql_mark=int(input("Enter your sql mark: "))
numpy_mark=int(input("Enter your numpy mark: "))
total=python_mark+sql_mark+numpy_mark
average=total/3

print("Name: ",name)
print("Age: ",age)
print("Python Mark: ",python_mark)
print("SQL Mark: ",sql_mark,"\nNumpy MArk: ",numpy_mark)
print("Total: ",total,"\nAverage: ",average)