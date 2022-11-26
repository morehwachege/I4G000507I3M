
class Animal:
    def __init__(self, name, age, park):
        self.name = name
        self.age = age
        self.park = park

    def get_details(self):
        return self.name, self.age, self.park

    def print_animal_details(self):
        print(self.name, self.age, self.park)

# obj = Animal()

class Lion(Animal):
    def __init__(self):
        Animal.__init__(self, name="Mr Lion", age=34, park="Kisumu Reserve")

    def print_something(self):
        return self.print_animal_details()




