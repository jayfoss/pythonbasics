#This is a special file that tells Python what this module loads and is loaded by default when the relative_import module is imported from other code

#Since we're importing files relative to us, but not submodules, we need to start the import name with a dot (relative to current directory).
#This puts everything in the some_cool_action file into the relative_import namespace
from .some_cool_action import *
#Import the submodule, in this case, submodule will get its own namespace within the relative_import module
from .submodule import *