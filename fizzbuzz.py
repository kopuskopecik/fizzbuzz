# Print numbers from 1 to 100 inclusively following these instructions:
# if a number is multiple of 3, print "Fizz" instead of this number,
# if a number is multiple of 5, print "Buzz" instead of this number,
# for numbers that are multiples of both 3 and 5, print "FizzBuzz",
# print the rest of the numbers unchanged.

numbers = range(1, 101)
for number in numbers:
    if number % 15 == 0:
        print(number, "is FizzBuzz")
    elif number % 5 == 0:
        print(number, "is Buzz")
    elif number % 3 == 0:
        print(number, "is Fizz")
    else:
        print(number, "unchanged")