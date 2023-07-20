# Convert Milliseconds Python Program

This Python program, `convert_milli.py,` provides two functions to convert a given number of milliseconds to a human-readable duration and a formatted date string. It allows users to input milliseconds and then display the converted results.

## Requirements

Python 3

## Usage

Steps:

1. Clone the repo.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `convert_milli.py`.
4. Run `python3 convert_milli.py.`
5. Enter the number of milliseconds when prompted.
6. The program will display the converted duration and date.

## Functions

### `convert_milliseconds_to_duration(milliseconds)`

This function takes the number of milliseconds as input and returns a human-readable string representing the duration in terms of years, days, hours, minutes, and seconds. It handles non-negative integer inputs and raises a `ValueError` if the input is invalid.

### `convert_milliseconds_to_date(milliseconds)`

This function takes the number of milliseconds as input and returns a formatted date string in the format 'YYYY-MM-DD HH:MM:SS.' It also handles non-negative integer inputs and raises a `ValueError` if the input is invalid.

## Example Usage

```python
import convert_milli

milliseconds_input = 1234567890
duration = convert_milli.convert_milliseconds_to_duration(milliseconds_input)
date = convert_milli.convert_milliseconds_to_date(milliseconds_input)

print(f"Converted Duration: {duration}")
print(f"Converted Date: {date}")
```

## Testing

To ensure the correctness of the `convert_milli.py` program, you can use the provided `tests.py` script or write your test cases using a testing framework like `unit test.`

## Note

I designed this program assuming the input will be a non-negative integer representing milliseconds. If you intend to use the functions for other types of inputs or additional error handling, you may need to modify the code accordingly.

## License

MIT
