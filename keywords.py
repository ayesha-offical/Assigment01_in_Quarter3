# Most frequently use special keywords of python which is important and special

#  1: if, elif, else (For conditions)
# 👉 Checks conditions and executes code accordingly.

age = 18
if age>= 18:
   print("you can vote!")
else:      
    print("You cannot vote.")

    #  2: for, while (For looping)
    # �� Loops through a sequence (like a list, tuple, string) or other iterable objects.

    for i in range(3):
      print("Hello!")

      count = 0
      while count < 3:
        print("Counting..", count)
        count += 1

# 3: def (Function definition)

# 👉 Used to define a function.

def greet(name):
    print("Hello, ", name)

greet("Ayesha Faisal")

# 4: return (Returns a value from a function)
# 👉 Sends back a value from a function.

def square (num):
   return num * num 

result = square(4)
print(result)

# 5: break, continue (Control loop execution)
# 👉 break stops the loop, continue skips the current iteration.

for i in range(5):
    if i == 3:
        break
    print(i)

    for i in range(5):
       if i == 3:
          continue
       print(i)

# 6: try, except (Error handling)
# 👉 Handles errors to prevent program crashes.

try:
   
   x = 15 / 0

except ZeroDivisionError:
    print("Cannot divide by zero!")

# 7:  class, object (Object-oriented programming)
# 👉 Defines a blueprint (class) and creates an instance (object).



class Car:
    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")
print(car1.brand)  


# 8: import (Imports modules)
# 👉 Brings external Python code into your program.

import math 

print(math.sqrt(30))


# 9: lambda (Anonymous function)
# 👉 Creates small, one-line functions

square = lambda x: x * x

print(square(8))


# 10: global, nonlocal (Variable scope)
# 👉 global modifies a variable outside a function, nonlocal affects a variable in the nearest enclosing function.

x = 10

def change_global():
    global x
    x = 20

change_global()
print(x)   

x = 10


# Python has a total of 35 reserved keywords (as of Python 3.10). These keywords have special meanings and cannot be used as variable names.
# Complete List of Python Keywords:

# .False
# .None
# .True
# a.nd
# .as
# .assert
# .async
# .await
# .break
# .class
# .continue
# .def
# .del
# .elif
# .else
# .except
# .finally
# .for
# .from
# .global
# .if
# .import
# .in
# .is
# .lambda
# .nonlocal
# .not
# .or
# .pass
# .raise
# .return
# .try
# .while
# .with
# .yield