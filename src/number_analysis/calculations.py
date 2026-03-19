# number_analysis/calculations.py

# --- Calculate average ---
def calculate_average(numbers):
    """Calculate the average of a list of numbers. Returns None if the list is empty."""
    if not numbers:
        return None
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return int(average) if average.is_integer() else round(average, 2)


# --- Calculate the median ---
def calculate_median(numbers):
    """Return the median of a list of numbers. Handles even and odd list lengths."""
    if not numbers:
        return None

    sorted_numbers = numbers.copy()
    count = len(sorted_numbers)

    # --- Bubble sort ---
    for pass_num in range(count):
        for i in range(0, count - pass_num - 1):
            if sorted_numbers[i] > sorted_numbers[i + 1]:
                sorted_numbers[i], sorted_numbers[i + 1] = (
                    sorted_numbers[i + 1],
                    sorted_numbers[i],
                )

    mid_index = count // 2
    if count % 2 == 0:
        median = (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2
    else:
        median = sorted_numbers[mid_index]

    if isinstance(median, float) and median.is_integer():
        median = int(median)
    else:
        median = round(median, 2)

    return median


# --- Find highest number ---
def find_highest(numbers):
    """Return the highest number in a list."""
    if not numbers:
        return None
    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
    return highest


# --- Find lowest number ---
def find_lowest(numbers):
    """Return the lowest number in a list."""
    if not numbers:
        return None
    lowest = numbers[0]
    for num in numbers:
        if num < lowest:
            lowest = num
    return lowest


# --- Count even and odd numbers ---
def count_even_odd(numbers):
    """Count the number of even and odd numbers in a list. Returns (even_count, odd_count)."""
    even_count = 0
    for num in numbers:
        if int(num) % 2 == 0:
            even_count += 1
    odd_count = len(numbers) - even_count
    return even_count, odd_count


# --- Generate summary ---
def generate_summary(numbers):
    """Return a dictionary summary with average, median, highest, lowest, even, and odd counts."""
    average = calculate_average(numbers)
    median = calculate_median(numbers)
    highest = find_highest(numbers)
    lowest = find_lowest(numbers)
    even_count, odd_count = count_even_odd(numbers)

    return {
        "average": average,
        "median": median,
        "highest": highest,
        "lowest": lowest,
        "even": even_count,
        "odd": odd_count,
    }
