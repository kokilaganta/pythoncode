import random

def generate_random_numbers(n):
    random_numbers = []
    for _ in range(n):
        random_numbers.append(random.randint(1, 100))
    
    total_sum = 0
    min_value = random_numbers[0]
    max_value = random_numbers[0]

    for num in random_numbers:
        total_sum += num
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    
    return random_numbers, total_sum, min_value, max_value

n = int(input("Enter the number of random numbers: "))
numbers, total_sum, min_value, max_value = generate_random_numbers(n)

print(f"Random Numbers: {numbers}")
print(f"Sum: {total_sum}")
print(f"Minimum Value: {min_value}")
print(f"Maximum Value: {max_value}")
