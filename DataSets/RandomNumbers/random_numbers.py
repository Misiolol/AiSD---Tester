import random
import os

def main():
    # Ensure the directory exists
    os.makedirs('./RandomNumbers', exist_ok=True)

    file_sizes = [10, 100, 400, 800, 1000, 4000, 8000, 10000, 40000, 80000, 100000, 400000, 800000, 1000000]
    for size in file_sizes:
        file_name = f'./RandomNumbers/numbers_{size}.txt'

        numbers = [str(random.randint(1, size * 10)) for _ in range(size)]
        
        with open(file_name, 'w') as f:
            f.write('\n'.join(numbers))
            f.write('\n')
            f.write('w\n')
        print(f'File {file_name} has been created with {size} random numbers.')

if __name__ == "__main__":
    main()