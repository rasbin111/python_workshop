class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age 
        self.address = address

    def print_info(self):
        print("Info: ")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

class Student(Person):

    def __init__(self, name, age, address, passed=True, marks=0):
        self.passed = passed
        self.marks = marks
        return super().__init__(name, age, address)

    def print_result(self):
        if self.passed:
            print(self.marks)


s1 = Student("rgt", 23, "Dolakha", True, 56)
print(f"Name: {s1.name} & Result: {s1.passed} & result: {s1.marks}")

class Parent:
    def greet(self):
        return "Namaste aakhum akhum"

class Child(Parent):
    def greet(self):
        return super().greet()

c1 = Child()
print(c1.greet())
