# Logic Builder - FizzBuzz with Counting

def fizz_buzz():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    for num in range(1, 51):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
            fizzbuzz_count += 1
        elif num % 3 == 0:
            print("Fizz")
            fizz_count += 1
        elif num % 5 == 0:
            print("Buzz")
            buzz_count += 1
        else:
            print(num)

    print("\n----- Summary -----")
    print(f"Fizz count: {fizz_count}")
    print(f"Buzz count: {buzz_count}")
    print(f"FizzBuzz count: {fizzbuzz_count}")


# Function call
fizz_buzz()