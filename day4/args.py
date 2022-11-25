# sys 
# import sys 
from sys import argv
from func import print_name
# print(argv)

def house():
    """"
    This is a house

    """
    return "This is another message about a house"


# def print_details():
#     # arguments = sys.argv
#     name = argv[1]
#     location = argv[2]
#     age = argv[3]
    
#     return f"{name}, {location}, {age}"

# print(__name__)


if __name__ == '__main__':
    # print(print_details())
    print_name("Mary", "Antoinnette")