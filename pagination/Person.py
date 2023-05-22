class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        sel.last_name = last_name

    def hello(self):
        print("hello!")

    def report(self):
        print(f"I am {self.first_name} {self.last_name}")


x = Person("John", "Smith")
x.report()
