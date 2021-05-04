dic = {
    'key-1': [
        'item-1' ,'item-2' ,'item-3'
    ],
    'key-2': 'String allowed',
    'key-3': True,
    'key-3': 1000
}

print(dic)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# immutable access ,means if keys changes will affect the x variable ,values & items functions is the same
x = car.keys()

print(x) #before the change

car["color"] = "white"
# update exiting item or add it
car.update({"years": [2019 ,2020 ,2021]})
# car['year'] = 'Update too'

print(x) #after the change

# key existence
if 'year' in car :
    print('Yes dictionary has the key "year" : ' + str(car["year"]))

"""
remove items :
del car["key-here"]
car.pop("key-here")
car.clear() for clear the whole dictionary
"""

for [key ,values] in car.items():
    print(key + " has :")
    print(values)
for item in car:
    print(item)
    print(car[item])

car_copy = car # means car_copy will be a reference to car if car changed car_copy will changed too
# best
car_copy = car.copy() # or dict(car)
car["year"] = "changed"
print(car_copy)

# nested dictionaries allowed too
# for more functions https://www.w3schools.com/python/python_dictionaries_methods.asp

cond1 = 'Ahmed' == 'ahmed'
cond2 = 2 == 1 + 0
if cond1:
    print("cond1 is true")
elif cond2:
    print('cond2 is true')
else:
    print('nothing is true')

i = 1
while i < 6:
    print(i)
    i += 1
else: # here we can we can duplicate if condition for several times once its not true else block will be invoked
    print("i is no longer less than 6")

# for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)

# functions is powerfull in python for advanced use check this link
# https://www.w3schools.com/python/python_functions.asp