# powerfull data strucutres

# dictionary dict(key_name=key_value) | {"key": "value"}
# is a hash map each key exists only 1 time
d = {
    "key_1": ['val 1' ,'val 2' ,'val 3' ,'val 4'],
    "key_2": ['val 5' ,'val 6' ,'val 7' ,'val 8']
}

# list its like array
l = ["apple", "banana", "cherry", "cherry" ,'bbb']

# tuple its like array too
t = ("apple", "banana", "cherry", "cherry" ,'bbb')

# set no duplication allowed
s = {"apple", "banana", "cherry", "cherry" ,'bbb'}


# Strings
s_1 = "Hello Worlds"
print(s_1[0:5]) # start from index 0 until letter before 5-1 : 4 => Hello

print(s_1[6:]) # start from index 6 until the end => Worlds

print(s_1[-6:]) # negative means start from the end

# some of String Methods
print(s_1.upper()) # capitalize the whole string
print(s_1.lower()) # lower all letters
print(" Hello ".strip()) # remove whitespaces from start and end
print(s_1.replace("H" ,'J')) # replace first appeaer of string by other one
print(s_1.split()) # split the string into list by token : default is space
# other string methods : https://www.w3schools.com/python/python_strings_methods.asp
print("String " + " Concatenable")

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
# here we use the format function to allow variables in string without concate them
# and we can set the parameter index {2} means take arg number 3 in func call