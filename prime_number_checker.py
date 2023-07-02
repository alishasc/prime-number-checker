can_divide = []  #add the numbers that divide into 'number'

def prime_checker(number):
    for num in range(1, number + 1):
        if number % num == 0: 
            can_divide.append(num)  #add to list
    print(f"These numbers can go into {number}: {can_divide}")
    if number == 1:
        print("It's not a prime number.")
    elif len(can_divide) > 2: 
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number = n)

