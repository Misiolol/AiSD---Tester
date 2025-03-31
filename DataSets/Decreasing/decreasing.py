import random
import time
import os

def generate_decreasing_sequence(n):
    num_range = n * 10 
    return sorted(random.sample(range(1, num_range + 1), n), reverse=True)

def save_sequence_to_file(n):
    directory = "./"
    os.makedirs(directory, exist_ok=True)
    filename = os.path.join(directory, f"decreasing_{n}.txt")
    sequence = generate_decreasing_sequence(n)
    with open(filename, "w") as f:
        f.write("\n".join(map(str, sequence)) + "\n")
        f.write("k\n")
    print(f"Saved decreasing sequence to {filename}")

def main():
    n_values = [10, 100, 400, 800, 1000, 4000, 8000, 10000, 40000, 80000, 100000, 400000, 800000, 1000000]
    for n in n_values:
        start_time = time.time()
        save_sequence_to_file(n)
        end_time = time.time()
        print(f"Generated sequence for n={n} in {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()