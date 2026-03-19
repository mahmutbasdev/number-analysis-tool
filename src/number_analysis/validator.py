# number_analysis/validator.py

# --- Check for stop keyword ---
def is_stop(user_input):
    """Check if the input string is the stop keyword. Returns True if 'stop', else False."""
    return user_input.lower() == "stop"

# --- Validate number input ---
def is_valid_number(user_input):
    """Convert input to a number if valid.

    Returns:
        int or float: the converted number if valid
        None: if input is invalid
    """
    try:
        value = float(user_input)
        value = round(value, 2)
        if value.is_integer():
            value = int(value)
        return value
    except ValueError:
        return None
