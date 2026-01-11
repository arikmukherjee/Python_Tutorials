thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict) 
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Using the dict() function to make a copy of a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}