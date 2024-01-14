#functions with inputs 
def greet(name, location):
    # name = input("What is your name?\n")
    print(f"Hello {name}")
    print(f"My current location is {location}")
greet("Angela", "Ikeja") #positional arguments
greet(name="Angela", location="Ikeja") #functional argument