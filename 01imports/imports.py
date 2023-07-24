#1. Module imports
#More info: https://docs.python.org/3/tutorial/modules.html
# - Mostly covered this
# - Modules are imported as follows: First try to locate things relative to the current folder
# - Then look at sys.path & PYTHONPATH (the environment variable which can be used to specify where on your system to find specific modules)
import relative_import
#Due to the way we organized the imports within relative_import's __init__, we can call this directly
relative_import.cool_function("COOL FUNCTION WAS CALLED")
#We can use submodules on this module
relative_import.submodule.submodule_function()