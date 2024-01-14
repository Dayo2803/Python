def prime(number):
    is_prime = True
    for i in range(2, number -1):
        if number % i == 0:
            is_prime = False
    if is_prime:
         print("It's a Prime number")
    else:
        print("Not a prime number")


prime_num = int(input("Input a number: "))
prime(number=prime_num)