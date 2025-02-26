# Data Types in Python

# There are 10 most using  Data Types in Python. They are:

# 1: Numeric Types 

#     a) Integer: A whole number without a fractional component. Examples: 1, -5, 2020.
#     b) Float: A number that has a fractional component. Examples: 3.14, -0.5, 0.0.

# 2. Sequence Types

#     a) String: A sequence of characters. Examples: "Hello", "Python", "2020".
#     b) List: A sequence of items. Examples: [1, 2, 3], ["apple", "banana", "cherry"].
#     c) Tuple: A sequence of items that cannot be changed. Examples: (1, 2, 3), ("apple", "banana", "cherry").
#     d) Range: A sequence of numbers. Examples: range(5), range(1, 5), range(1, 10, 2).

# 3. Set Types

#     a) Set: A collection of unique items. Examples: {1, 2, 3}, {"apple", "banana", "cherry"}.
#     b) frozenset: A collection of unique items that cannot be changed. Examples: frozenset({1, 2, 3}), frozenset({"apple", "banana", "cherry"}).

# 4. Mapping Types

#     a) dict: A collection of key-value pairs. Examples: {"name": "John", "age": 30}, {"fruit": "apple", "color": "red"}.

# 5. Boolean Types

#     a) bool: Represents a boolean value. Examples: True, False.



# Example of Numeric Types

# Integer

x : int=456

print(type(x))
print("This is a example of intiger: ",x)

# Float

y:float=4.90

print(type(y))
print("This is a example of Float: ",y)



# Example of Sequence Types

# String

a:str="Hello Python"

print(type(a))
print("this is example of String: ",a)

# List

b:list=[1,2,3,4,5,6]

print(type(b))
print("This is a example of list: ",b)


# Tuple

c:tuple=(1,2,3,4,5,6)

print(type(c))
print("This is a example of Tuple :",c)


# Range

print(list(range(1, 21)))

# Example of Set Types

# Set (Set does not allow duplicates).

d:set={1,2,3,3,4,4,5,6}

print(type(d))
print("This is a example of Set: ",d)

# frozenset

e:frozenset=frozenset({1,2,3,45,45,45,45})

print(type(e))
print ("This is a Example of Frozenset: ",e)

# Example of Mapping Types

# dict

f:dict[str,str]={"name": "Ayesha Mughal", "age": 17,"Slot":"Monday 2:00 - 5:00"}
print (type(f))
print("This is a example of dict: ",f)

# Example of Boolean Types

g:bool=True

print(type(g))
print("This is a example of Boolean: ",g)
