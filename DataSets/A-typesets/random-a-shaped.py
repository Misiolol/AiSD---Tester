import random
import time

def generate_a_shaped_sequence(n):
    mid = n // 2 + n % 2
    increasing_part = sorted(random.sample(range(1, 10 * n + 1), mid))
    decreasing_part = sorted(random.sample(range(1, 10 * n + 1), n - mid), reverse=True)
    return increasing_part + decreasing_part

def save_sequence_to_file(n):
    filename = f"a_shaped_{n}.txt"
    sequence = generate_a_shaped_sequence(n)
    with open(filename, "w") as f:
        f.write("\n".join(map(str, sequence)) + "\n")
        f.write("k\n")
    print(f"Saved A-shaped sequence to {filename}")

if __name__ == "__main__":
    n_values = [10, 100, 1000, 4000, 8000, 10000, 40000, 80000, 100000]
    for n in n_values:
        start_time = time.time()
        save_sequence_to_file(n)
        end_time = time.time()
        print(f"Generated sequence for n={n} in {end_time - start_time:.4f} seconds")
