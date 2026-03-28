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

    return median, sorted_numbers

def calculate_Q1(numbers):
    """Return the Q1 of a list of numbers."""
    if not numbers:
        return None

    _, sorted_numbers = calculate_median(numbers)

    mid_index = len(sorted_numbers) // 2
    lower_half = sorted_numbers[:mid_index]

    q1,_ = calculate_median(lower_half)
    return q1


def calculate_Q3(numbers):
    """Return the Q3 of a list of numbers."""
    if not numbers:
        return None

    _, sorted_numbers = calculate_median(numbers)

    mid_index = len(sorted_numbers) // 2
    upper_half = sorted_numbers[mid_index:]
    
    if len(numbers) % 2 == 0:
        upper_half = sorted_numbers[mid_index:]
    else:
        upper_half = sorted_numbers[mid_index + 1]
        
    q3, _ = calculate_median(upper_half)
    return q3


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
    """Return a dictionary summary with average, Q1, median, highest, lowest, even, and odd counts."""
    average = calculate_average(numbers)
    median,_ = calculate_median(numbers)
    q1 = calculate_Q1(numbers)
    q3 = calculate_Q3(numbers)
    highest = find_highest(numbers)
    lowest = find_lowest(numbers)
    even_count, odd_count = count_even_odd(numbers)

    return {
        "average": average,
        "q1": q1,
        "q3": q3,
        "median": median,
        "highest": highest,
        "lowest": lowest,
        "even": even_count,
        "odd": odd_count,
    }
