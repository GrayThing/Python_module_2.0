import random

first_plate = random.choice(range(3, 21))


def get_password(number):
    password = ''
    for number_first in range(1, 21):
        for number_second in range(1, 21):
            if number_first < number_second and first_plate % (number_first + number_second) == 0:
                password = password + str(number_first) + str(number_second)
    return password


print(f'Password for the first plate with number {first_plate} is {get_password(first_plate)}')

