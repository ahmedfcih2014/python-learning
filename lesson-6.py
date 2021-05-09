x = lambda arg1 ,arg2 : arg1 * arg2

print(x(2 ,5))

arr = [
    "apple",
    'orange',
    'drinks'
]

arr.append('pinapple')

print(arr)

# for more function for array (list) check this link : https://www.w3schools.com/python/python_arrays.asp array method section

# creating class
class Person:
    # defined attributes
    name = 'Welcome'
    age = -1
    gender = 'Male'

    # constructor
    def __init__(self ,name):
        self.name = name

    def setAge(self ,age):
        self.age = age

    def setName(self ,name):
        self.name = name

    def setGender(self ,gender):
        self.gender = gender

    def greeting(self):
        return 'Welcome there ,my name is ' + self.name

ali = Person('Ali Hesham')
ali.setAge(14)
ali.setGender('Male')
print(ali.greeting())

# inheritance
class Student(Person):
    def __init__(self ,graduationYear):
        super().__init__('Student')
        self.graduationYear = graduationYear

    def getGraduationYear(self):
        return self.graduationYear

ahmed = Student(2023)
ahmed.setName('Ahmed Hesham')

print(ahmed.greeting())
print("Ahmed graduation year is : " + str(ahmed.getGraduationYear()))