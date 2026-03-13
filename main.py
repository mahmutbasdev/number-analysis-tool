from sys import exit
from tkinter import Tk, filedialog
import os

print("Welcome to the number analysis program.")


# --- Choose input method ---
def choose_input_method():
    print("Choose input method:")
    print("1 - Manual input")
    print("2 - Import CSV file")
    choice = input("Enter your choice: ")
    return choice


numbers = []


# --- Check for stop keyword ---
def is_stop(user_input):
    return user_input.lower() == "stop"


# --- Validate number input ---
def is_valid_number(user_input):
    try:
        value = float(user_input)
        value = round(value, 2)
        if value.is_integer():
            value = int(value)
        return value
    except ValueError:
        return None


# --- Calculate average ---
def calculate_average(numbers):
    if not numbers:
        return None
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return int(average) if average.is_integer() else round(average, 2)

# --- Calculate the median ---
def calculate_median(numbers):
    if not numbers:
        return None

    count = len(numbers)

    # --- Bubble sort: manually sort the list ---
    for pass_num in range(count):
        for i in range(0, count - pass_num - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

    mid_index = count // 2

    if count % 2 == 0:
        median = (numbers[mid_index - 1] + numbers[mid_index]) / 2
    else:
        median = numbers[mid_index]

    if isinstance(median, float) and median.is_integer():
        median = int(median)
    else:
        median = round(median, 2)

    return median


# --- Find highest number ---
def find_highest(numbers):
    if not numbers:
        return None
    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
    return highest


# --- Find lowest number ---
def find_lowest(numbers):
    if not numbers:
        return None
    lowest = numbers[0]
    for num in numbers:
        if num < lowest:
            lowest = num
    return lowest


# --- Count even and odd numbers ---
def count_even_odd(numbers):
    even_count = 0
    for num in numbers:
        if int(num) % 2 == 0:
            even_count += 1
    odd_count = len(numbers) - even_count
    return even_count, odd_count


# --- Generate summary ---
def generate_summary():
    average = calculate_average(numbers)
    median = calculate_median(numbers)
    highest = find_highest(numbers)
    lowest = find_lowest(numbers)
    even_count, odd_count = count_even_odd(numbers)

    summary = {
        "average": average,
        "median": median,
        "highest": highest,
        "lowest": lowest,
        "even": even_count,
        "odd": odd_count,
    }
    
    return summary


# --- Export results to CSV ---
def export_to_csv(summary, filename="results.csv"):
    file_exists = os.path.exists(filename)
    with open(filename, "a") as file:
        if not file_exists:

            file.write(",".join(summary.keys()) + "\n")
        file.write(",".join(str(value) for value in summary.values()) + "\n")


# --- Print results ---
def print_results(numbers):
    print("\nAnalysis complete")
    print(f"Entered numbers: {numbers}")
    print(f"Total count: {len(numbers)}")
    if not numbers:
        print("No numbers to analyze.")
        return

    summary = generate_summary()

    for key, value in summary.items():
        print(f"{key.capitalize()}: {value}")

    export_to_csv(summary)


# --- Manual input loop ---
def manual_input():
    print("Type numbers. When you want to stop, type 'stop'.")
    while True:
        user_input = input()
        if is_stop(user_input):
            print_results(numbers)
            exit(0)
        result = is_valid_number(user_input)
        if result is not None:
            numbers.append(result)
        else:
            print("Please enter only valid numbers!")


# --- CSV import with file picker ---
def import_csv():
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


# --- Main program ---
choice = choose_input_method()

if choice == "1":
    manual_input()
elif choice == "2":
    numbers = import_csv()
    print_results(numbers)
else:
    print("Invalid choice.")
