myList = ["Apple" ,"Banana" ,"Cherry" ,"Pinapple" ,'Watermelon']
__myList = [
    ["Apple" ,"Banana" ,"Cherry" ,"Pinapple" ,'Watermelon'],
    ["Apple" ,"Banana" ,"Cherry" ,"Pinapple" ,'Watermelon'],
    ["Apple" ,"Banana" ,"Cherry" ,"Pinapple" ,'Watermelon']
]

# get by index
print(myList[1])

# get range
print(myList[1:])

# check item existence
print ("Apple" in myList)

# index change
myList[0] = "New Apple"
print(myList)

# range change
myList[2:4] = ["New Cherry" ,"New Pinapple"]
print(myList)

# add item to selected index and shift other items ,allowed access from both sides (positive or negative)
myList.insert(1 ,"Shifted")
print(myList)

# append item to the end of a list
myList.append("at the END")
print(myList)

newL = ['AAA' ,'AAAA']

# append list (collection : tuples ,sets & dictionaries) to other one
myList.extend(newL)
print(myList)

# remove item from specific index
myList.pop(2)
print(myList)
del myList[0]
print(myList)

# remove item by value
myList.remove("AAAA")
print(myList)

# clear the whole list
myList.clear()
print(myList)

# List Comprehension
def loopList(l):
    [print(x) for x in l]
[loopList(x) for x in __myList]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# generating new list from list depend on a boolean condition
newlist = [x for x in fruits if "a" in x]
print(newlist)

# list is sortable by sort() or reverse() and its able to use a custom function for sorting
# newL = oldL.copy() : this means take a copy to new list
# newL = list(oldL) : same as previous line

l1 = ["a" ,"b" ,"c" ,"d" ,"e"]
l2 = ["f" ,"g" ,"h" ,"i" ,"j"]
l3 = l1 + l2
print(l3)

# list method here https://www.w3schools.com/python/python_lists_methods.asp