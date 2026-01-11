def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(name): # name is a parameter
  print("Hello", name)
my_function("Emil") # "Emil" is an argument


# Default Arguments
def my_function(country = "Norway"):
  print("I am from", country)
my_function("Sweden")
my_function("India")
my_function()  # uses the default value "Norway"
my_function("Brazil")

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function(animal = "dog", name = "Buddy")


def my_function(fruits):
  for fruit in fruits:
    print(fruit)
my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits) # passing a list as an argument

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])
my_person = {"name": "Emil", "age": 25} # passing a dictionary as an argument
my_function(my_person)

def my_function(x, y):
  return x + y
result = my_function(5, 3)
print(result)

def my_function(name, /):
  print("Hello", name)
my_function("Emil")