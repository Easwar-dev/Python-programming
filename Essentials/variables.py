# variable accessbility is three types
# public protected private

# public is accessible from anywhere
# protected is accessible within Family (class & subclasses)
# private is accessible only by itself(strictly internal, critical data)

class Myclass:
    def __init__(self):
        self.__private_variable = "I am Private"

    def show_private(self):
        return self.__private_variable

obj = Myclass()
# print(obj.__private_variable)  # error AttributeError
print(obj.show_private())        # Access through method

# Name Mangling for private variables
# In Python, private variables are not truly private.
# They can still be accessed from outside the class using a technique called name mangling.
class My_2nd_Class:
    def __init__(self):
        self.__private_var = "I am Private"

    def show_private(self):
        return self.__private_var

obj = My_2nd_Class()
# Accessing private variable using name mangling
print(obj._My_2nd_Class__private_var)  # ✓ Access using name mangling

# Accessing private method
class My_3rd_Class:
    def __init__(self):
        self.__private_var = "I am Private"

    def __private_method(self):
        return "This is a private method"

    def show_private(self):
        return self.__private_var + " and " + self.__private_method()

obj = My_3rd_Class()
print(obj.show_private())    # ✓ Access through method
# print(obj.__private_method())  # ✗ AttributeError
print(obj._My_3rd_Class__private_method())  # ✓ Access using name mangling