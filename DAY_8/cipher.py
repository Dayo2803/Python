alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




# def encrypt(plain_text, amount_shift):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + amount_shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"the cipher text {cipher_text}")

# def decrypt(cipher_text, amount_shift):
#     plain_txt = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - amount_shift
#         plain_txt += alphabet[new_position]
#     print(f"The decrypted text {plain_txt}")

# if direction == 'encode':
#     encrypt(plain_text=text, amount_shift=shift)
# elif direction == 'decode':
#     decrypt(cipher_text=text, amount_shift=shift)

# from art import logo
# print(logo)
# def ceasar(start_txt, amount_shift, cip_dir):
#     end_text = ""
#     for letter in start_txt:
#         position = alphabet.index(letter)
#         if cip_dir == 'decode':
#             amount_shift *= -1
#         new_position = position + amount_shift
#         end_text += alphabet[new_position]
#     print(f"The {cip_dir} text {end_text}")

# ceasar(start_txt=text, amount_shift=shift, cip_dir=direction)

to_continue = True
while to_continue:

    direction = input("TYpe 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25

    from art import logo
    print(logo)
    def ceasar(start_txt, amount_shift, cip_dir):
        end_text = ""
        if cip_dir == 'decode':
            amount_shift *= -1
        for char in start_txt:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + amount_shift
                end_text += alphabet[new_position]
            else:
                end_text += char
        print(f"The {cip_dir} text {end_text}")

    ceasar(start_txt=text, amount_shift=shift, cip_dir=direction)

    con = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if con == 'no':
        to_continue = False
        print("Goodbye!")