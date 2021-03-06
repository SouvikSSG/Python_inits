"""
Copyright (c) 2020, Souvik Ghosh.

Distributed under the terms of the MIT License.

The full license is in the file LICENSE, distributed with this software.

Created on Feb 20, 2020

@author
"""

class Names:
    counter = 0  # it is the class variable

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Names.counter += 1  # it adds first then print
        print("Object is created:", Names.counter)

    def __str__(self):  # it returns the updated string of 'self.fullname'
        self.fullname = "{} {}".format(self.name, self.surname)
        return self.fullname

    def printing_name(self):
        return "My full name is {}".format(self.fullname)

    @classmethod
    def class_var(cls):  # this function is reference to the class
        # can be accessed by 'Names.class_var() and
        # 'Names().class_var() both.
        return cls.counter


name_obj_1 = Names('Souvik', 'Ghosh')  # it will take arguments in __init_
# now it will run what is defined in __init__()

print(Names.counter)

print(Names.class_var())  # as 'class_var()' is reference to the class,
# we can write like this.

name_obj_2 = Names('Guido', 'Van')  # it will run __init__() again

print(Names.counter)

print(Names.class_var())

print(name_obj_1)  # it will return all the dunder method used in class
# for this object 'name_obj_1
print(Names.printing_name(name_obj_1))  # accessing with class

print(name_obj_2)  # returns all dunder for this object 'name_obj_2'

print(Names.printing_name(name_obj_2))

print(name_obj_1.printing_name())  # we are accessing function defined
# inside the class
print(name_obj_2.printing_name())

print(name_obj_1.fullname)  # we want to print a specified value of the
# attribute of this class
print(name_obj_2.fullname)

## attributes can't be accessed using class like 'class.attribute'
## but, it can accessed using object like 'class().attribute'
## where, object=class().
print(dir(Names))
