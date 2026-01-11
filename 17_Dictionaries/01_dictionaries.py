thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(thisdict["brand"]) # Output: Ford

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020     # Duplicate key; the last value will overwrite the previous one
}
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
print(len(thisdict)) # Output: 3

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"] # List as a value
}
print(thisdict) # Output: {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict)) # Output: <class 'dict'>