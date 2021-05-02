# hint : its useless if we need to update its content
# data strucute that's not editable at all
myTuple = ("Banana" ,"Apple" ,"Apple")
print(myTuple)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

[print(x) for x in thistuple]

t1 = (1 ,2 ,3 ,4 ,5)
t2 = (1 ,2 ,3 ,4 ,5)
# join tuples
t3 = t1 + t2
print(t3)
# duplicate items in tuples by n
n = 2
print(t1 * n)

# to count value existsence
print(myTuple.count("Apple"))

# data strucute that's not order and not changeable
# Once a set is created, you cannot change its items, but you can add new items.
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
print("pinapple" in thisset)

thisset.add("pinapple")
print(thisset)

# bulk add (by any iterable DS)
thisset.update(["Apple" ,"Orange"])
print(thisset)

# remove an unkown item
# because its not ordered this means it will get a random item and remove it from the set
print(thisset.pop())
print(thisset)

[print(x) for x in thisset]

# to join sets can use any of the next functions
"""
union or update : s1.union(s2) | s1.update(s2)
intersection_update : will keep the duplicated values only
intersection : s1.intersection(s2) will keep only values from s1 and the duplicated values from s1 in s2
symmetric_difference_update : s1.symmetric_difference_update(s2) unique values in each set
usefull set functions : https://www.w3schools.com/python/python_sets_methods.asp
"""