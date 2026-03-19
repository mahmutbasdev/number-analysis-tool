# number_analysis/io.py

import os
from tkinter import Tk, filedialog
from number_analysis.validator import is_stop, is_valid_number
from number_analysis import calculations


def choose_input_method():
    """Ask the user how they want to provide numbers: manual or CSV."""
    print("Choose input method:")
    print("1 - Manual input")
    print("2 - Import CSV file")
    choice = input("Enter your choice: ")
    return choice


def manual_input():
    """Collect numbers from user input until 'stop' is typed. Returns a list of numbers."""
    numbers = []
    print("Type numbers. When you want to stop, type 'stop'.")
    while True:
        user_input = input()
        if is_stop(user_input):
            break
        value = is_valid_number(user_input)
        if value is not None:
            numbers.append(value)
        else:
            print("Please enter only valid numbers!")
    return numbers


def import_csv():
    """Open a file dialog and import numbers from a CSV file. Returns a list of numbers."""
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    file_path = filedialog.askopenfilename(
        title="Select CSV file", filetypes=[("CSV Files", "*.csv")]
    )
    if not file_path:
        print("No file selected.")
        return []

    imported_numbers = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                value = is_valid_number(line)
                if value is not None:
                    imported_numbers.append(value)
                else:
                    print(f"Skipping invalid value: {line}")
    except FileNotFoundError:
        print("File not found.")
        return []

    return imported_numbers


def print_results(numbers):
    """Print analysis results and export them to CSV."""
    if not numbers:
        print("No numbers to analyze.")
        return

    print("\nAnalysis complete")
    print(f"Entered numbers: {numbers}")
    print(f"Total count: {len(numbers)}")

    summary = calculations.generate_summary(numbers)

    for key, value in summary.items():
        print(f"{key.capitalize()}: {value}")

    export_to_csv(summary)


def export_to_csv(summary, filename="results.csv"):
    """Append analysis summary to a CSV file in the 'data' folder."""
    file_path = os.path.join("data", filename)
    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as file:
        if not file_exists:
            file.write(",".join(summary.keys()) + "\n")
        file.write(",".join(str(value) for value in summary.values()) + "\n")
