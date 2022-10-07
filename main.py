from art import logo
from turtle import clear
print(logo)

#Calculator
def add ( x, y):
  return x + y

def subtract ( x, y):
  return x - y

def multiply ( x, y):
  return x * y

def division ( x, y):
  return x / y

operations ={ 
  "+": add,
  "-" : subtract, 
  "*" : multiply, 
  "/": division
}  

def calculator ():
  num1 = float(input ("what is the first number?:  "))
  for symbol in operations:
    print (symbol)

  should_continue = True  

  while should_continue:
    operation_symbol = input("Pick and operation: ")
    num2 = float(input("What is the next number?:  "))
    calculation_funcion = operations[operation_symbol]
    answer = calculation_funcion(num1, num2)

    print( f"The  result is: {num1} {operation_symbol} {num2} = {answer} ")

    yes_no_exit = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation or type 'e' to exit: ") 

    if yes_no_exit == "y":
      num1 = answer
      
    elif yes_no_exit == "n":
      calculator()
    else:
      should_continue = False
calculator()      







#Here we select "*"  which overides the "+" we  leceted above


#Here the calculation_function selected will be the multiply() function
#calculation_funcion = operations[operation_symbol]

#Here the code will be
# second_answer = multiply(multiply(nim1, num2), num3)
#second_answer = calculation_funcion(calculation_funcion(num1, num2),num3)
#second_asnwer = 2* 3 * 3 = 18

#To fix this bug we nedd to change the code in line 46
#second_answer = calculation_funcion(first_answer, num3)

#print(f"The last result is :{first_answer} {operation_symbol} {num3} = {second_answer}")