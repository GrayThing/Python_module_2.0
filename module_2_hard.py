import random

n = random.choice(range(3, 21))


def get_password(number):
    result = ''
    for number_first in range(1, 21):
        for number_second in range(1, 21):
            if number_first < number_second and n % (number_first + number_second) == 0:
                result = result + str(number_first) + str(number_second)
    return result


print(f'Password for the first plate with number {n} is {get_password(n)}')

