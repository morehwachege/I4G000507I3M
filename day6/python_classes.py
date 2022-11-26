class Animal:
    """This a class that prints information about an animal"""
    def __init__(self, name, age, genus, park):
        self.name = name
        self.age = age
        self.genus = genus
        self.park = park


    def print_name(self):
        return (self.name,
                self.age,
                self.genus,
                self.park)

# obj = Animal("King Lion", 7, "lionicae", "Nairobi National Park")
# print(obj.print_name())

class Lion(Animal):
    def __init__(self, has_partner, shed):
        self.has_partner = has_partner
        self.shed = shed
        Animal.__init__(self, "Lion King", 34, "beast", "Boni reserve")
    
    def print_from_above(self):
        print(self.has_partner)

# linked lists
# list
# binary search
# hash, queues
# tree

obj = Lion(True, "Kilimani shed")
print(obj.print_from_above())