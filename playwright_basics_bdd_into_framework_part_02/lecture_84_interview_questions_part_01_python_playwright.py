# =============== Question 0 ========================
"""


ANSWER:


"""
# =============== Question 01 ========================
"""
What is the difference between list and tuple?

ANSWER:
    List is mutable whereas tuple is immutable. That means, we can update, modify, delete the elements
    of a list, but we cannot perform any modification to tuple. See the example below

"""
from operator import truediv

my_name_list = ["Nazmul", "Mahe", "Alam", 32, 46]
print(my_name_list)

# Adding "Rabbi" into the list
my_name_list.append("Rabbi")
# Printing new list
print(my_name_list)

# Removing 46 from the list
my_name_list.remove(46)
# Printing new list
print(my_name_list)

# Tuple
my_not_changeable_tuple = ("Musarrat", "Jahan", "Kumu")

# my_not_changeable_tuple.remove("Kumu") => This code will not work as once tuple is declared, cannot be
# modified
print(my_not_changeable_tuple)

# =============== Question 02 ========================
"""
What are the data types in python?

ANSWER:
    numeric  = integer, float, complex
    boolean = true, false
    diction = key: value pair
    set =   set, frozenset [sets do not support indexing, slicing, or other sequence-like behavior.]
            set =   mutable, unique elements, unorder values( no indexing like list or tuple)
            frozenset = immutable, 
    sequence type = list, tuple, string 
"""

a = 5
b = 10.5
c = 10 + 5j
sleep = True
wake = False
dic_type_data = {"Name": "Nazmul", "Age": 32}
my_list = {"You", "Me,", "He", "She"}
my_tuple = ("value", "unchangeable", "in", "tuple")

# =============== Question 03 and 04  ========================
"""
    How do you implement inheritance and super keyword in python?
    
   

ANSWER:
    Basically, inheritance means acquiring the property of parents class to child class. When parent
    class is called in child class, child class can access the properties of parent class such as 
    attributes, variables, methods. See the below example.
    
    and super keyword is used in child class to call or use the attributes of parent class

"""
# =============== Question 5 ========================
"""
    What is the purpose of __init__ and self keyword in python?

ANSWER:
    __init__ 
    
    is used when we want to initialized the constructor of a class. A class can have 
    have only one constructor. If constructor is not defined that the built in constructor of that 
    class is called. However, default constructor does not have any argument [ def __init__(self) ]
    but we can provide argument in our constructor and also can give implementation. 
    
    
    "self"
    
    has multiple usages. 
    
    1)If we want to access the instance variables (constructor variables), inside the
    class to use them in methods, or for other use, we can call the constructor variables using "self"
    key word like "self.variable_name"
    
    class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
    
    2) If we want to modify the instance variables in class such as 
    
    class Employee:
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name
        
    3) If we want to call a method into another method in the same class
    
    class Employee:
    def greet(self):
        print("Hello")

    def welcome(self):
        self.greet()
        
    
    
    4) to create instance variables 
    class Employee:
    def __init__(self, name):
        self.name = name
        self.age = 31
        
    [ Without self, the variables would be local to the method and disappear after it finishes. ]
"""


# This a parent class which will be called in child class
class ParentClass:
    def greetings(self):
        print("Hello, my child class can access me")

    def greetings_from_parent_class(self):
        print("Hello, I come from parent class")


# Proving the parent class name into the parameter of child class so that child class can have access to
# parent class properties
class ChildClass(ParentClass):

    def __init__(self, your_name):
        self.your_name = your_name

    def greetings_from_child_class(self):
        print("Hello, I come from child class")

    # child class modified the parent class and used it
    def greetings_from_parent_class(self):
        print("Hello, I come from parent to child class")

        super().greetings_from_parent_class()

    # calling the instance variable (constructor variable)
    def calling_parameter_constructor_method(self):
        print("Hello, my name is " + self.your_name)


#   [[[ ------- REMEMBER: Python does not support constructor overloading ------]]]


# The child class is expecting an argument
child_object = ChildClass("Kumu")
# Accessing its own method
child_object.greetings_from_child_class()
# Accessing parent method
child_object.greetings()
# Modified the method by calling from parent class and used object to call from child class
child_object.greetings_from_parent_class()

child_object_with_parameter = ChildClass("Nazmul Mahe Alam")

child_object_with_parameter.calling_parameter_constructor_method()

# =============== Question 6 ========================
"""
    How to read and write a file in python ?

ANSWER:


"""

# To read a file first argument open the file in its location and second argument give "r" as read
# store as an object "f"
with open("//playwright_basics_bdd_into_framework_part_02"
          "/data/read_text.txt", "r") as f:
    # reading the whole text file
    read_context = f.read()
    # print in console
    print("\n" + read_context)

# To write a file, frist open the file and select , mode write (w) and store as an "f" object and
# use write method
with open("//playwright_basics_bdd_into_framework_part_02"
          "/data/write_text.txt", "w") as f:
    write_context = f.write(" I am writing this line in write_text.txt file in this project."
                            "\nThis process is used to write something in a file."
                            "\nGo and check the file write_text.txt")

# =============== Question 08 ========================
"""
    How to create a list of dictionaries in python?

ANSWER:
        In python we declare list like this "people_age = [ 32,34,35]" and dictionary is declared like
        "people_details = { "name" : "Bob", "age" : 34, "address" : "45 sunrise ave"}
        So the list of dictionaries will be like below variable

"""
people_details = [
    {"name": "Kumu", "Age": 23, "Address": " 45 Sunrise Ave"},
    {"name": "Nazmul", "Age": 32, "Address": "51A NorthWood"},
    {"name": "Utsob", "Age": 21, "Address": "03 Pathorghata"}
]

# It is going to the index 02 which is ""name": "Utsob", "Age": 21, "Address": "03 Pathorghata"" then
# it is searching for "Address" and prints "03 Pathorghata"
print(people_details[2]["Address"])

# =============== Question 09 ========================
"""
    What is lamda function?

ANSWER:
        A lambda function is an anonymous function ( nameless function ) that can have multiple
        arguments but only one expression ( one executable line such as x+y, return x*x, etc)
        It is written when we need to call a function for one time. In UI automation, when
        a dialog box pops up, we normally use lambda function to accept reject a javascript dialog
        which cannot be handled by playwright.
        See the below example:
       
        def test_confirm_popup(page):
            page.goto("https://rahulshettyacademy.com/AutomationPractice/")

            page.on("dialog",lambda dialog: dialog.accept())

            page.locator("#confirmbtn").click()

"""


# Without lambda the function looks like below

def add_two_numbers(x, y):
    return x + y


print("Regular Function sum up", add_two_numbers(2, 3))

# Storting the return addition of 2 numbers in add_two variable
# means "add_two" is a variable but storing as function type, like variable stores int, string type
add_two = lambda x, y: x + y
add = 5

#
print("When used lambda function:", add_two(2, 3))
# Its type is function
print(type(add_two))
# its is type is integer
print(type(add))


#       ::::::::::REMEMBER::::::

"""
When interviewers ask:

What are first-class objects in Python?

        Python treats functions as first-class objects, meaning they can be assigned to variables,
        passed as arguments, returned from functions, and stored in data structures.

Are functions the only first-class objects?


        No. Integers, strings, lists, dictionaries, classes, class instances, and functions 
        are all objects in Python. Functions are specifically highlighted because Python allows them 
        to be manipulated just like any other object.
        
"""


def greet():
    print("Hello")


# output -> <function greet at 0x103d43530> means "This is a function named "greet"
#                                           stored at memory address 0x103d43530"
print(greet)

# Here the function is called to execute
print(greet())


# =============== Question 10 ========================
"""
        
        How to apply map(), filter(), , sort(), in lambda function ?

ANSWER:


"""
# MAPS:

number_list = [1, 2, 3, 4, 5]

# So, what this lambda function is doing, it is taking an argument x and returns x*x.
# However, map( lambda_expression, name_of_theList) is taking first argument as lambda expression
# and representing the argument "x" in each of the elements of "number_list" and at the end,
# we are converting everything in new list storing. map is used when we want to modify all the elements
# of a list
new_number_square_list = list(map(lambda x: x*x, number_list))
print("The new square list: ", new_number_square_list)


# FILTER:


# filter is used when based on a condition, we want to filter the elements of a list
# what this below code is doing, it is lambda finds the elements from " new_number_square_list"
# which can be divided by 2 and make a list of those elements and stores in
# "even_list_from_square_numbers"
even_list_from_square_numbers = list(filter(lambda x: x % 2 == 0, new_number_square_list))

# This will print only 4 and 16
print("After filtering new square list is :", even_list_from_square_numbers)


# SORT:

sequence_number = [20, 11, 19, 25, 9, 7, 23]

# sorting the "sequence_number" and also storing the new list in same variable name "sequence_number"
sequence_number = sorted(sequence_number)
print(sequence_number)


