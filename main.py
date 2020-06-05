def add(num1, num2):
  return num1 + num2
def subtract(num1, num2):
  return num1 - num2
def multiply(num1, num2):
  return num1 * num2
def divide(num1, num2):
  return num1 / num2

print(""" Select one of the operations:

1. Addition
2. Subtraction
3. multiply
4. Division
5. Powers
6. Remainders""")

select = int(input('Which operation do you need?1/2/3/4/5/6: '))

num1 = int(input('Please enter your first number: '))
num2 = int(input('Please enter your second number: '))

if select == 1:
  print(num1, '+', num2, '=', add(num1, num2))
elif select == 2:
  print(num1, '-', num2, '=', subtract(num1, num2))
elif select == 3:
  print(num1, 'x', num2, '=', multiply(num1, num2))
elif select == 4:
  print(num1, '/', num2, '=' , divide(num1, num2))
elif select == 5:
  print(num1, '^', num2, '=', num1**num2)
elif select == 6:
  print(num1, 'R', num2, '=',  num1 % num2)
else:
  print("Invalid input!")