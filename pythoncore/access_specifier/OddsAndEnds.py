__author__ = 'veradocs-web'

class Employee:
    """Inside Employee Class"""
    def __init__(self):
        pass

john = Employee() # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

print john.__dict__ #convert Object to dict
print john.__class__
print john.__doc__
print john.__module__
print john.__init__()






