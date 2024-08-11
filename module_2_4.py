numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers[1:]:
    is_prime = True
    for j in range(2, len(numbers)):
        if i % j == 0 and i != j:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print('Primes: ', primes)
print('Not primes: ', not_primes)