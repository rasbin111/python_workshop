class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


    def printPersonInfo(self):
        print(f"{self.name}, {self.age}, {self.address}")


class Employee(Person):
    def __init__(self, name, age, address, salary, post):
        super().__init__(name, age, address)
        self.salary = salary
        self.post = post


    def printEmpoyeeInfo(self):
        print(f"{self.name}, {self.age}, {self.address}, {self.post}, {self.salary}")


if __name__ == "__main__":
    e1 = Employee("rasbin", 27, "Mati, Dolakha", 25000, "Engineer")
    e1.printEmpoyeeInfo()
