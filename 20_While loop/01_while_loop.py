i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# The output will be:
# 1
# 2
# 4
# 5
# 6

i = 1
while i < 6:
  print(i)
  i += 1
else:  # executed when the condition becomes false
  print("i is no longer less than 6")
# The output will be:
# 1
# 2
# 3
# 4
# 5
# i is no longer less than 6