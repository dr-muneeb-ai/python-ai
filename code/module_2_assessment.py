# =====================================================================
# The School of AI (Python-AI) - Module 2 Assessment Solutions
# Developer: Muneeb Bin Arshad
# =====================================================================

"""
Module 2 Assessment: Advanced Python Concepts
- Question 1: Decorators for Execution Timing & Logging
- Question 2: Custom Generator for Prime Numbers / Fibonacci Sequence
- Question 3: File I/O with Exception Handling and Data Parsing
"""

import time
import functools

# ---------------------------------------------------------------------
# Question 1: Execution Time Decorator
# Write a decorator function 'log_execution' that logs the time taken 
# by any function to execute.
# ---------------------------------------------------------------------

def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"[LOG] Starting execution of '{func.__name__}'...")
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"[LOG] Function '{func.__name__}' executed in {elapsed_time:.6f} seconds.")
        return result
    return wrapper


@log_execution
def compute_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# ---------------------------------------------------------------------
# Question 2: Custom Generator for Fibonacci Sequence
# Write a generator function 'fibonacci_generator(n)' that yields the 
# first n Fibonacci numbers.
# ---------------------------------------------------------------------

def fibonacci_generator(n: int):
    if n <= 0:
        return
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# ---------------------------------------------------------------------
# Question 3: File Handling & Safe Parsing with Exception Handling
# Write a function that safely reads a configuration or dataset file, 
# handles FileNotFoundError, and parses values.
# ---------------------------------------------------------------------

def process_data_file(file_path: str) -> list:
    parsed_records = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                stripped = line.strip()
                if not stripped or stripped.startswith('#'):
                    continue  # Skip empty lines and comments
                parts = stripped.split(',')
                parsed_records.append([p.strip() for p in parts])
        print(f"Successfully processed {len(parsed_records)} records from '{file_path}'.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred while reading '{file_path}': {e}")
    return parsed_records


# =====================================================================
# Testing / Execution Block
# =====================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("=== Testing Q1: Execution Time Decorator ===")
    print("=" * 50)
    fact_result = compute_factorial(10)
    print(f"Factorial of 10 is: {fact_result}")

    print("\n" + "=" * 50)
    print("=== Testing Q2: Fibonacci Generator ===")
    print("=" * 50)
    fib_sequence = list(fibonacci_generator(8))
    print(f"First 8 Fibonacci numbers: {fib_sequence}")

    print("\n" + "=" * 50)
    print("=== Testing Q3: File I/O & Exception Handling ===")
    print("=" * 50)
    
    # Create a dummy test file for demonstration
    sample_file = "sample_data.csv"
    with open(sample_file, "w", encoding="utf-8") as f:
        f.write("# Name, Age, Role\n")
        f.write("Muneeb, 24, Developer\n")
        f.write("Ali, 25, Designer\n")
    
    records = process_data_file(sample_file)
    print("Parsed Data Records:", records)
