def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

print("-----")

def my_function(*args):
  print("Type:", type(args)) # Shows that args is a tuple 
  print("First argument:", args[0]) # Accessing the first argument
  print("Second argument:", args[1]) # Accessing the second argument
  print("All arguments:", args) # Printing all arguments
my_function("Emil", "Tobias", "Linus")

print("-----")

def my_function(greeting, *names):
  for name in names:
    print(greeting, name)
my_function("Hello", "Emil", "Tobias", "Linus")
#output:
# Hello Emil
# Hello Tobias
# Hello Linus

print("-----")

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total
print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))