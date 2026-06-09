def list_operation(x, y, n):
# Use list comprehension to generate the list of numbers divisible 
    return [num for num in range(x, y + 1) if num % n == 0]
