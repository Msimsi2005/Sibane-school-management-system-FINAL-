# utils.py
# Small helper functions to keep code clean and simple.

def pause():
    # Function for non-blocking pause: simply print a blank line so the
    # UI returns immediately to the menu without waiting for input.
    print()  # Print blank line

def print_line():
    # Function to print a line to separate UI sections.
    print("-" * 50)  # Print 50 dashes
