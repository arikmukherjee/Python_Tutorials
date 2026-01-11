thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] 
print(x)  # Output: Mustang

# Using the get() method to access an item
y = thisdict.get("year")
print(y)  # Output: 1964

x = thisdict.keys()
print(x)  # Output: dict_keys(['brand', 'model', 'year'])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change # Output: dict_keys(['brand', 'model', 'year'])
car["color"] = "white"
print(x) #after the change # Output: dict_keys(['brand', 'model', 'year', 'color'])

x = thisdict.values()
print(x)  # Output: dict_values(['Ford', 'Mustang', 1964])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change # Output: dict_values(['Ford', 'Mustang', 1964])
car["year"] = 2020
print(x) #after the change # Output: dict_values(['Ford', 'Mustang', 2020])

x = thisdict.items()
print(x)  # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
car["year"] = 2020
print(x) #after the change # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")  
  # Output: Yes, 'model' is one of the keys in the thisdict dictionary