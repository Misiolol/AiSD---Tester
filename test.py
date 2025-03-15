import subprocess
import os
import time
import pandas as pd
import matplotlib.pyplot as plt

def read_setup_config(setup_file):
    config = {}
    if os.path.isfile(setup_file):
        with open(setup_file, "r") as f:
            for line in f:
                line = line.strip()
                if '=' in line:
                    key, value = line.split('=')
                    config[key.strip()] = value.strip()
    else:
        print(f"Error: '{setup_file}' not found.")
    return config

def run_executable_with_multiple_inputs(executable, input_files, output_excel_file, output_chart_files, plots_enabled):
    if not os.path.isfile(executable):
        print(f"Error: '{executable}' not found.")
        return

    random_results = []
    vtype_results = []
    atype_results = []
    
    for index, input_file in enumerate(input_files):
        if not os.path.isfile(input_file):
            print(f"Error: Input file '{input_file}' not found. Skipping...\n")
            continue

        print(f"Running '{executable}' with input from '{input_file}'...\n")

        with open(input_file, "r") as infile:
            input_lines = infile.readlines()

        input_data = "".join(input_lines)

        run_cmd = [f"./{executable}"]
        if os.name == "nt":
            run_cmd = [executable]

        start_time = time.time()

        run_process = subprocess.run(run_cmd, input=input_data, capture_output=True, text=True)

        end_time = time.time()
        execution_time = end_time - start_time

        num_lines = len(input_lines)

        print("Program Output:\n")
        print(run_process.stdout)
        print("Error Output (if any):\n")
        print(run_process.stderr)
        print(f"Execution Time: {execution_time:.6f} seconds")
        print("-" * 50)

        if index == 0:
            print(f"Skipping '{input_file}' from final results...\n")
            continue  

        if 'Random' in input_file:
            random_results.append({
                "Number of Numbers in File": num_lines,
                "File Name": input_file,
                "Execution Time (seconds)": execution_time
            })
        elif 'V' in input_file:
            vtype_results.append({
                "Number of Numbers in File": num_lines,
                "File Name": input_file,
                "Execution Time (seconds)": execution_time
            })
        elif 'A' in input_file:
            atype_results.append({
                "Number of Numbers in File": num_lines,
                "File Name": input_file,
                "Execution Time (seconds)": execution_time
            })

    random_df = pd.DataFrame(random_results)
    vtype_df = pd.DataFrame(vtype_results)
    atype_df = pd.DataFrame(atype_results)

    with pd.ExcelWriter(output_excel_file, engine='openpyxl') as writer:
        random_df.to_excel(writer, sheet_name='Random', index=False)
        vtype_df.to_excel(writer, sheet_name='V-Type', index=False)
        atype_df.to_excel(writer, sheet_name='A-Type', index=False)
    print(f"Results have been saved to '{output_excel_file}'.")

    if plots_enabled:
        if not random_df.empty:
            plt.figure(figsize=(10, 6))
            plt.plot(random_df["Number of Numbers in File"], random_df["Execution Time (seconds)"], marker='o', linestyle='-', color='b')
            plt.title("Execution Time vs. Number of Numbers (Random)")
            plt.xlabel("Number of Numbers in File")
            plt.ylabel("Execution Time (seconds)")
            plt.grid(True)
            plt.savefig(output_chart_files["Random"])
            plt.show()
            print(f"Random plot has been saved to '{output_chart_files['Random']}'.")

        if not vtype_df.empty:
            plt.figure(figsize=(10, 6))
            plt.plot(vtype_df["Number of Numbers in File"], vtype_df["Execution Time (seconds)"], marker='o', linestyle='-', color='g')
            plt.title("Execution Time vs. Number of Numbers (V-Type)")
            plt.xlabel("Number of Numbers in File")
            plt.ylabel("Execution Time (seconds)")
            plt.grid(True)
            plt.savefig(output_chart_files["V-Type"])
            plt.show()
            print(f"V-Type plot has been saved to '{output_chart_files['V-Type']}'.")

        if not atype_df.empty:
            plt.figure(figsize=(10, 6))
            plt.plot(atype_df["Number of Numbers in File"], atype_df["Execution Time (seconds)"], marker='o', linestyle='-', color='r')
            plt.title("Execution Time vs. Number of Numbers (A-Type)")
            plt.xlabel("Number of Numbers in File")
            plt.ylabel("Execution Time (seconds)")
            plt.grid(True)
            plt.savefig(output_chart_files["A-Type"])
            plt.show()
            print(f"A-Type plot has been saved to '{output_chart_files['A-Type']}'.")

setup_file = "setup.py"
config = read_setup_config(setup_file)

random_enabled = config.get('random', 'False') == 'True'
Vtype_enabled = config.get('Vtype', 'False') == 'True'
Atype_enabled = config.get('Atype', 'False') == 'True'
plots_enabled = config.get('plots', 'False') == 'True'

input_files = []
if random_enabled:
    input_files.extend(["./DataSets/RandomNumbers/numbers_10.txt", "./DataSets/RandomNumbers/numbers_100.txt", "./DataSets/RandomNumbers/numbers_1000.txt", "./DataSets/RandomNumbers/numbers_4000.txt", "./DataSets/RandomNumbers/numbers_8000.txt", "./DataSets/RandomNumbers/numbers_10000.txt", "./DataSets/RandomNumbers/numbers_40000.txt", "./DataSets/RandomNumbers/numbers_80000.txt","./DataSets/RandomNumbers/numbers_100000.txt"])
if Vtype_enabled:
    input_files.extend(["./DataSets/V-typesets/v_shaped_10.txt", "./DataSets/V-typesets/v_shaped_100.txt", "./DataSets/V-typesets/v_shaped_1000.txt", "./DataSets/V-typesets/v_shaped_4000.txt", "./DataSets/V-typesets/v_shaped_8000.txt", "./DataSets/V-typesets/v_shaped_10000.txt", "./DataSets/V-typesets/v_shaped_40000.txt", "./DataSets/V-typesets/v_shaped_80000.txt", "./DataSets/V-typesets/v_shaped_100000.txt"])
if Atype_enabled:
    input_files.extend(["./DataSets/A-typesets/a_shaped_10.txt", "./DataSets/A-typesets/a_shaped_100.txt", "./DataSets/A-typesets/a_shaped_1000.txt", "./DataSets/A-typesets/a_shaped_4000.txt", "./DataSets/A-typesets/a_shaped_8000.txt", "./DataSets/A-typesets/a_shaped_10000.txt", "./DataSets/A-typesets/a_shaped_40000.txt", "./DataSets/A-typesets/a_shaped_80000.txt", "./DataSets/A-typesets/a_shaped_100000.txt"])

output_excel_file = "execution_results.xlsx"
output_chart_files = {
    "Random": "random_execution_time_chart.png",
    "V-Type": "vtype_execution_time_chart.png",
    "A-Type": "atype_execution_time_chart.png"
}

executable_file = "a.exe"
run_executable_with_multiple_inputs(executable_file, input_files, output_excel_file, output_chart_files, plots_enabled)
