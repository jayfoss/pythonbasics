print('=== Classes ===')
#We can declare basic classes
class Test:
    #We skipped the __init__ function which is our constructor so nothing happens once this class is created, until we start calling functions on it

    #We can add functions to them. self is a special parameter which at runtime is given the value of the instance of the object
    def my_func(self):
        print('test')

    #We used a default argument here
    def set_coolness(self, coolness = 0):
        self.coolness = coolness

#Create instances of them
t = Test()
#And call functions on them
t.my_func()

t.set_coolness()
#We can directly read the value of instance variables in Python
print(t.coolness)

#And we can directly set the value of instance variables
t.coolness = -1
print(t.coolness)

t.set_coolness(5.3)
print(t.coolness)

t2 = Test()
t2.set_coolness(4.9)

#Variables are unique to the instance of the object they are on
print(t.coolness)
print(t2.coolness)

print('=== Constructors ===')
#We can create classes with constructors that set up default values we want to give variables when the instances is created using __init__
class TestWithConstructor:
    def __init__(self):
        self.coolness = 5.0

#We called no methods on t3, yet it has a coolness of 5.0
t3 = TestWithConstructor()
print(t3.coolness)

print('=== Inheritance - Subclasses ===')
#We can inherit from classes and get all the methods from the parent class in the child class (subclass)
class TestWithInheritance(Test):
    pass

t4 = TestWithInheritance()
t4.my_func()

print('=== Subclasses with Overrides ===')

#We can inherit from classes and get all the methods from the parent class automatically added to the new class, but we can also override them
class TestWithInheritanceOverride(Test):
    def my_func(self):
        print('overrode my_func')

    #We can also add new methods
    def my_func_that_doesnt_exist_on_parent(self):
        print('I was added')

t5 = TestWithInheritanceOverride()
t5.my_func()
t5.my_func_that_doesnt_exist_on_parent()

print('=== Polymorphism - Subclasses being treated as parents ===')

#We can pass subclasses around as if they were parent classes and get complex functionality by calling methods or accessible variables we know exist in the parent class,
#and using their unique behaviour
def print_some_stuff(an_instance_of_test):
    an_instance_of_test.my_func()
    #THIS WOULD FAIL AS IT WOULD TRY TO CALL IT ON 't' WHICH IS THE PARENT AND DOESN'T HAVE THIS FUNCTION
    #an_instance_of_test.my_func_that_doesnt_exist_on_parent()

print_some_stuff(t)
print_some_stuff(t5)

print('=== Super ===')
#We can even call functionality from the parent class directly using super(), even if we override the method in our subclass
class TestWithSuper(Test):
    def my_func(self):
        super().my_func()
        print('I was printed too')

t6 = TestWithSuper()
t6.my_func()