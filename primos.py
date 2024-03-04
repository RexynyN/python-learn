from math import sqrt

def primes_primes_more_primes(threshold):
    number = 3
    primes = [2]
    i = 1 
    while i < threshold:        
        guard = True
        root = sqrt(number)
        # "If a number is not divisible by all primes less or equal than the square root of it, it's a prime"
        for j in primes:
            if j > root:
                break 

            if number % j == 0:
                guard = False
                break
        
        if guard:
            primes.append(number)
            i += 1

        number += 1

    for prime in primes:
        print(str(prime), end=" ")

if __name__ == "__main__":
    import argparse 

    parser = argparse.ArgumentParser()
    parser.add_argument("threshold", type=int, default=10000, help="Number of primes to return")

    args = parser.parse_args()

    primes_primes_more_primes(args.threshold)
