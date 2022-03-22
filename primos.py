from math import ceil

# Mude essa váriavel  para retornar uma lista de n primeiros números primos
threshold = 10000

number = 3
primes = [2]
i = 1 
while i < threshold:        
    guard = True
    for j in range(2, ceil(number/2) + 1):
        if(number % j == 0):
            guard = False
            break
    
    if guard == True:
        primes.append(number)
        i += 1

    number += 1

print(str(primes))