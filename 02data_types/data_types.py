#Python has many data types
#lists - can be changed after being created, store many arbitrary values of multiple types. Common operations include iteration (looping over)
#Use lists when you just want to store a bunch of values, e.g. all your items in a todo list
my_list = [1, 'cat', 'something', 0, 1]
print(my_list)
print(type(my_list))

my_int = 5
print(my_int)
print(type(my_int))

my_float = 5.6
print(my_float)
print(type(my_float))



#A complex type also exists but it's unlikely to be important to you



#Strings can be created using single or double quotes
my_string = 'My cool string'
my_double_quoted_string = "My cool string"
print(my_string)
print(my_double_quoted_string)
print(type(my_string))
print(type(my_double_quoted_string))

#Using double quotes allowed me to write the single quote inside without it breaking the string by thinking I'd typed an end quote.
#Putting f before a string allows you to insert variables in squiggly braces
my_f_string = f"here's my float {my_float}"
print(my_f_string)

#Because I used single quotes here, I had to escape the inner apostrophe with a backslash (since it's the same character as a single quote) or it would end the string
my_f_string2 = f'here\'s my int {my_int}'
print(my_f_string2)

#Generally, single or double quotes are fine in Python for strings, just pick a convention for your project and stick to it


my_bool = True
print(my_bool)
print(type(my_bool))

#tuples - cannot be changed after being created (are immutable), store many arbitrary values of multiple types.
#Use tuples when you just want to efficiently store a bunch of values that never change. You can also use them as return types from functions to return multiple values from a function easily
my_tuple = ('hi', 0, 4, 'lo')
print(my_tuple)
print(type(my_tuple))

#Dictionaries (dicts) - store key, value pairs. These are great if you need to arbitrarily retrieve values from specific keys at random as if you have a key,
#you can look up a value in constant time. With a list you would have to iterate each item until you have found the value you want which for large lists can be expensive
my_dict = {'key1': 0, 'key2': 5}
print(my_dict)
print(type(my_dict))

#Sets - Store values, but will de-duplicate them. Also only immutable types such as integers, floats, booleans, tuples and strings are allowed to be values
#Order is not guaranteed in sets and mathematical concepts such as unions can be applied to them
my_set = {1, 2, 5, 2, 2, 2, 3, 'hi'}
print(my_set)
print(type(my_set))

#There are other data types but other than objects which we will cover later, these should cover most cases


#Some comparison important notes
print('=== Booleans and Numbers ===')
print(True == 1) #This is True
print(False == 0) #This is True
print(True == 1.0) #This is True
print(type(1.0))
print(False == 0.0) #This is True

print("=== Equality Considerations ===")

print('123' == '123') #Strings can be safely compared for equality
print([1, 2, 3] == [1, 2, 3]) #Lists can be safely compared for equality
print([1, 2, 3] == [1, 3, 2]) #False as not same order
print({'key1': 0, 'key2': 5} == {'key2': 5, 'key1': 0}) #Dicts can be safely compared for equality
print({'key1': 0, 'key2': 5} == {'key2': 5, 'key1': 1}) #Dicts can be safely compared for equality

print("=== Classes & Objects ===")
#Basic class definition, we covered this in detail on our call
class Test:
    def __init__(self, name):
        self.name = name

my_class_instance1 = Test('name1')
my_class_instance2 = Test('name1')
print(my_class_instance1 == my_class_instance2) #Despite these both looking identical, they cannot be safely compared as in this case == compares the location in memory of the 2 objects
#not the value of the object instance so you would only use == on objects if you want to check if they're precisely the same instance
var_to_compare = my_class_instance1
print(var_to_compare == my_class_instance1) #This is True as var_to_compare was assigned to the same instance as my_class_instance1


class Test2:
    def __init__(self, name):
        self.name = name


#However, you can override a special method on classes, __eq__ which takes in the self instance and another value (the instance to compare against) which allows you to define
#how to properly compare 2 instances of this object for equality
    def __eq__(self, __value):
        return __value.name == self.name
    
my_class2_instance1 = Test2('name1')
my_class2_instance2 = Test2('name1')
print(my_class2_instance1 == my_class2_instance1) #In this case, this returns True as rather than comparing memory locations, I have told Python that Test2 instances are compared for equality
#by checking if the name variable is equal
