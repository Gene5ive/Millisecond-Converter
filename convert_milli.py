import datetime
from datetime import datetime

# Function to convert milliseconds to a human-readable duration string
def convert_milliseconds_to_duration(milliseconds):
    # Check if the input is a non-negative integer
    if not isinstance(milliseconds, int) or milliseconds < 0:
        raise ValueError("Milliseconds must be a non-negative integer.")
    
    # Calculate the time units (years, days, hours, minutes, and seconds)
    seconds = int((milliseconds / 1000) % 60)
    minutes = int((milliseconds / (1000 * 60)) % 60)
    hours = int((milliseconds / (1000 * 60 * 60)) % 24)
    days = int((milliseconds / (1000 * 60 * 60 * 24)) % 365)
    years = int((milliseconds / (1000 * 60 * 60 * 24 * 365)))

    # Create a list to hold the time units
    time_units = []

    # Append years to the list if greater than 0
    if years > 0:
        time_units.append(f"{years} year{'s' if years != 1 else ''}")

    # Append days to the list if greater than 0
    if days > 0:
        time_units.append(f"{days} day{'s' if days != 1 else ''}")

    # Append hours to the list if greater than 0
    if hours > 0:
        time_units.append(f"{hours} hour{'s' if hours != 1 else ''}")

    # Append minutes to the list if greater than 0
    if minutes > 0:
        time_units.append(f"{minutes} minute{'s' if minutes != 1 else ''}")

    # Append seconds to the list if greater than 0
    if seconds > 0:
        time_units.append(f"{seconds} second{'s' if seconds != 1 else ''}")

    # Check if any time units were added to the list
    if len(time_units) == 0:
        return "0 seconds"

    # Join the time units into a single string and return
    return ", ".join(time_units)

# Function to convert milliseconds to a formatted date string
def convert_milliseconds_to_date(milliseconds):
    # Check if the input is a non-negative integer
    if not isinstance(milliseconds, int) or milliseconds < 0:
        raise ValueError("Milliseconds must be a non-negative integer.")
    
    # Convert milliseconds to a datetime object and format it as a string
    return datetime.fromtimestamp(milliseconds / 1000).strftime('%Y-%m-%d %H:%M:%S')

try:
    # Get user input for the number of milliseconds
    milliseconds_input = int(input("Enter the number of milliseconds: "))

    # Call the conversion functions
    duration = convert_milliseconds_to_duration(milliseconds_input)
    date = convert_milliseconds_to_date(milliseconds_input)

    # Print the results
    print(f"\nConverted Duration: {duration} \nConverted Date: {date}")

except ValueError as ve:
    # Catch and handle the ValueError if the input is invalid
    print(f"Error: {ve}")

except Exception as e:
    # Catch and handle any other unexpected errors
    print(f"An unexpected error occurred: {e}")
