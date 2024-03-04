import colorama
from colorama import init
init()
import math

# TODO: Add a message telling which song is being processed at the moment
def progressbar(progress, total, message="", color=colorama.Fore.YELLOW):
    percent = 100 * (progress / float(total))
    # # A larger bar, if you need xD
    # bar = '█' * int(percent) + "-" * (100 - int(percent))

    bar = '█' * int(percent/2) + "-" * (50 - int(percent/2))
    print(color + f"\r|{bar}| {percent:.2f} {message}", end="\r")
    if progress == total:
        print(colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f} {message}", end="\r")

numbers = [x * 5 for x in range(2000, 3000)]
results = []

progressbar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progressbar(i + 1, len(numbers), message=f"| Sexozinho gostoso por {i} vezes")
