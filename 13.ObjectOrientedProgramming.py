class Employee:
    __name = None               # double underscore means these are variables and they are private
    __id = 0
    __salary = 0
    __grade = 'SG6'

    # This is how we create constructor
    def __init__(self, name, id, salary, grade):
        self.__name = name              # The self parameter is a reference to the current instance of the class, and
        self.__id = id                  # is used to access variables that belongs to the class.
        self.__salary = salary
        self.__grade = grade

    # Getter Setter
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_grade(self):
        return self.__grade

'''Mayur = Employee()
Mayur.set_name("Mayur")
print(Mayur.get_name())
Mayur.set_id("1")
print(Mayur.get_id())
print(Mayur.get_grade())'''

Raj = Employee("Raj", "2", "100000", 'govtEmp')
print(Raj.get_name())
print(Raj.get_id())
print(Raj.get_grade())