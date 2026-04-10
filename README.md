# Number Analysis

A Python project for analyzing lists of numbers. You can enter numbers manually or import them from a CSV file to calculate basic statistics.

## Features

- Calculate average, median, Q1, Q3 highest, and lowest numbers

- Count even and odd numbers

- Manual input or CSV import

- Export results automatically to results.csv

- All calculations done manually, no built-in functions for core statistics

Results are immediately exported to data/results.csv after analysis.
If the file does not exist, it will be created automatically.

## Usage

1. Open your terminal.

2. Run the analysis script from the project root:

### Windows PowerShell
```bash
$env:PYTHONPATH="src"
python -m scripts.run_analysis
```
### Linux/macOS
```bash
export PYTHONPATH=src
python -m scripts.run_analysis
```
#### Input methods

1. Manual input – Type numbers, then type stop to finish.

2. CSV import – Select a CSV file containing numbers.

Results are printed in the terminal and automatically saved to results.csv.


## Run Unit Tests

1. Open your terminal.

2. Run the unittest from the project root:

### Windows PowerShell
```bash
$env:PYTHONPATH="src"
python -m unittest tests/test_calculate_median.py
```

### Linux/macOS
```bash
export PYTHONPATH=src
python -m unittest tests/test_calculate_median.py
```

## Purpose

This project serves as an introduction to data analysis with Python.
By implementing calculations without using built-in functions, it helps you understand exactly how averages, medians, maxima/minima, and even/odd counts are computed.

## What I Learned

- Implementing basic statistics manually (average, median, max/min, even/odd counts)

- Validating user input and handling exceptions

- Reading from and writing to CSV files

- Structuring a Python project clearly for reuse and testing

- Writing and running unit tests to verify functionality


