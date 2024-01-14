program_dict ={
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}
program_dict["Loop"] = "The action of doing something overa nd over again"

# program_dict = {}
# print(program_dict)
# editing an item in a dictionary
# program_dict["Bug"] = "The action of doing something overa nd over again"
# print(program_dict)

#looping through a dictionary
for key in program_dict:
    print(key)
    print(program_dict[key])
