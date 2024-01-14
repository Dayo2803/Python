#len deos not work with integers
num_char = len(input("what is your name?"))

#convert an integer into a string
num_char_cpy = str(num_char)

print("Your name has " + num_char_cpy + " characters.")

a = float(123)
print(a)

print(70 + float("100.5"))

print(str(70) + str(100))


#addition of two numbers
two_digit_number = input("Type a two digit number: ")
first_num = int(two_digit_number[0])
second_num = int(two_digit_number[1])
two_digit_number = first_num + second_num
print(two_digit_number)