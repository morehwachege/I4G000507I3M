# class 

def name():
    """" This function prints a name"""
    print("Ortega")

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    
    def woof(self):
        print("Woof")


    def print_details(self):
        # return f"{self.name}, {self.age}"
        return self.name, self.age

obj = Animal("Ken", 34)
print(obj)

print(obj.print_details())
