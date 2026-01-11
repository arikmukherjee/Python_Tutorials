thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)         # prints the keys
print("-----")

for x in thisdict:
  print(thisdict[x])  # prints the values
print("-----")

for x in thisdict.values():
  print(x)  # prints the values
print("-----")

for x in thisdict.keys():
  print(x)  # prints the keys
print("-----")

for x, y in thisdict.items():
  print(x, y) # prints both keys and values