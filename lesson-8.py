import json

json_string =  '{ "name":"John", "age":30, "city":"New York"}'

parsed = json.loads(json_string)

print(parsed)

# convert python DS to json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# for json usage by python : https://www.w3schools.com/python/python_json.asp

# for regex : https://www.w3schools.com/python/python_regex.asp

# pip is a python package manager : https://www.w3schools.com/python/python_pip.asp

z = "asd"

try:
    print(z)
except:
    print("Z is not defined")
else:
    print("no exception raised")
finally:
    print("try except ,block executed all")

name = input("What is your name ?")
print(name)