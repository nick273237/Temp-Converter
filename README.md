# Temperature-Converter

A simple Python command-line program that converts temperatures between Celsius (C) and Fahrenheit (F) with input validation and limited retry attempts.

## Features
### Convert:
- Celsius > Fahrenheit
- Fahrenheit > Celsius
### Input validation for:
- Numeric temperature values
- Valid unit (C or F)
- Retry system with limited attempts
- Clean output formatting (removes unnecessary decimals)
## How It Works
- The user enters a temperature.
- The program checks if the input is valid:
- Allows up to 5 attempts for correct input.
- The user enters the unit (C or F):
- Allows up to 5 attempts.
- The temperature is converted.
- The result is formatted and displayed.
## Optional Improvements
- Add Kelvin conversion
- Continuous conversion loop
- GUI version
