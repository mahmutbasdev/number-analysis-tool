# run_analysis.py

from number_analysis import choose_input_method, manual_input, import_csv, print_results

def main():
    print("Welcome to the number analysis program.")

    choice = choose_input_method()

    if choice == "1":
        numbers = manual_input()
    elif choice == "2":
        numbers = import_csv()
    else:
        print("Invalid choice.")
        return

    print_results(numbers)


if __name__ == "__main__":
    main()
