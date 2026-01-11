thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative indexing means start from the end
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #cherry
#Range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #['cherry', 'orange', 'kiwi']
print(thislist[:4]) #['apple', 'banana', 'cherry', 'orange']
print(thislist[3:]) #['orange', 'kiwi', 'melon', 'mango']
#Range of negative indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #['orange', 'kiwi', 'melon']

#Check if item exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")