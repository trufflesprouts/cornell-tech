
def find_index(numbers, value):
    """
    Write a function that takes a list and a value,
    and returns the index of the value in the list.
    If the value is not in the list, return -1.
    Do not use the built-in .index() method for this problem.
    """
    for i, current_value in enumerate(numbers):
        if current_value == value:
            return i
    return -1

def categorize_number(n):
    """
    Write a function that categorizes the given number as 'negative', 'zero', or 'positive'.
    """
    if n < 0:
        return 'negative'
    if n == 0:
        return 'zero'
    if n > 0:
        return 'positive'
    pass

def reverse_list(numbers):
    """
    Write a function that returns the reversed version of a list without using the built-in reverse method.
    """
    n = len(numbers)
    reversed_list = [0] * n
    for i, value in enumerate(numbers):
        reversed_list[n-i-1] = value
    return reversed_list

def process_numbers(numbers):
    """
    Write a function that takes a list of numbers.
    The function should iterate through the list and print each number until it encounters a negative number,
    at which point it should break out of the loop. If it encounters a zero, it should skip that iteration using the continue statement.
    """
    for number in numbers:
        if number < 0:
            break
        if number == 0:
            continue
        print(number)
    pass

def string_lengths(strings):
    """
    Given a list of strings, write a function that returns a dictionary where the keys are the strings and the values are the lengths of those strings.
    """
    dict = {}
    for string in strings:
        dict[string] = len(string)
    return dict

def even_values_keys(data):
    """
    Given a dictionary, write a function that returns a list of keys whose values are even numbers.
    """
    even_keys = []
    for key, value in data.items():
        if value % 2 == 0:
            even_keys.append(key)
    return even_keys

def square_evens(numbers):
    """
    Given a list of numbers, use a list comprehension to return a list of squares of even numbers.
    """
    return [n ** 2 for n in numbers if n % 2 == 0]

def long_strings(strings):
    """
    Given a list of strings, use a list comprehension to return a list of strings that have a length greater than 5.
    """
    return [s for s in strings if len(s) > 5]

def convert_to_celsius(fahrenheit_temps):
    """
    Convert a list of temperatures from Fahrenheit to Celsius.

    Given a list of temperatures in Fahrenheit, convert each temperature to Celsius.
    If the temperature is below freezing (32°F or 0°C), append the string "Freezing"
    to the converted temperature. Otherwise, just return the converted temperature.

    Formula for Conversion:
    Celsius = (Fahrenheit - 32) / 1.8

    Example:
    Input: [32, 50, 100, 0, 20]
    Output: ['0.0°C Freezing', '10.0°C', '37.8°C', '-17.8°C Freezing', '-6.7°C Freezing']
    """
    celsius_temps = []
    for temp_f in fahrenheit_temps:
        temp_c = round((temp_f - 32) * 5/9, 1)
        celsius_temps.append(
            f'{temp_c}°C Freezing' if temp_c <= 0 else f'{temp_c}°C'
        )
    return celsius_temps
