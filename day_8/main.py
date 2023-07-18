# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Let's go")

# greet()

# def greet_with_name(name):
#     print("How are you " + name)
#     print(f'How are you feel {name}')
#     print('Bye ' + name)

# greet_with_name("Julek")

# def greet_with_name_and_location(name, location):
#     print(f"Hello {name}.")
#     print(f"Do you came from {location} ?")
    
# greet_with_name_and_location(location="Poznań", name="Julek")

#Area calculating

# test_h = int(input("Write the height of room: \n"))
# test_w = int(input("Write the width of room: \n"))
# coverage = 5

# def paint_area(heigh, width, cover):
#     number_of_can = (heigh * width) / cover
#     print(round(number_of_can))

# paint_area(test_h, test_w, coverage)

#Prime number checker
number = int(input("Write number to check: \n"))
def check_num(num):
    if num == 1:
        print(f"This number {num} is not prime number.")
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print(f"{num} this number is prime.")
    else:
        print(f"{num} this number is not prime.")
        
check_num(number)