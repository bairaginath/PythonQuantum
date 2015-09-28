__author__ = 'veradocs-web'


print(globals()) #Return a dictionary representing the current global symbol table.


# Update and return a dictionary representing the current local symbol table.
# Free variables are returned by locals() when it is called in function blocks, but not in class blocks.
print(locals())