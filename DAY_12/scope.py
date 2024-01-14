# enemies = 1 #global declaration
# def inrease_enemies():
#     # global enemies #not advisabel
#     # enemies += 2 #local declaration
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1

# enemies = inrease_enemies()
# print(f"enemies outside function: {enemies}")

#local scope

#no block scope in python
# game_level = 3
# def create_enemy():
#     enemies = ["scorpion", "alien", "mouse"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy)

# Global variable are very useful for constant

pi = 3.14159
# def calc()

def bar():
    my_variable = 9
 
    if 16 > 9:
      my_variable = 16
 
    print(my_variable)
 
bar()