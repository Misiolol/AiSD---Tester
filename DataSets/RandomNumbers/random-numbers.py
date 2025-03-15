import random

# Define the file paths
file_sizes = [10, 100, 1000, 4000, 8000, 10000, 40000, 80000, 100000]
for size in file_sizes:
    file_name = f'numbers_{size}.txt'
    # Generate random numbers
    numbers = [str(random.randint(1, 999999)) for _ in range(size)]
    
    # Write the numbers to a file
    with open(file_name, 'w') as f:
        f.write('\n'.join(numbers))
        f.write('\n')
        f.write('\n'.join("w"))
    print(f'File {file_name} has been created with {size} random numbers.')