#Basic Programming terminology
Function, Method, Procedure: All very similar with minute details, for most purposes you can use these terms interchangeably. Procedures are just Functions that don't return a value. Methods are Functions associated with classes usually

Invoke or Call a function: Execute (run it). You will Call a function with Arguments that you pass in

Assignment: Setting a value to a variable. Python doesn't have variable declaration and initialization as some languages do but if I use these terms anywhere, they should be considered as synonymous to "the first assignment of a variable"

Arguments vs Parameters: Parameters are the values a function expects to receive and are defined when you write the function (basically a blueprint for what values a function requires). Arguments are the actual values you pass to a function for each parameter. Python supports default arguments so functions can be defined like
```python
def my_func(val1, val2=True):
  pass
```
When calling my_func, the parameter val1 is required and will error if no argument is provided for it, but val2 can be safely ommitted

The keyword pass in Python is a no-op (an operation that does nothing). You can use it as a placeholder if you want to write a function definition but don't want to actually write code in it yet. The interpreter complains if you have empty functions with no content as it can't parse them properly
```python
pass
```
