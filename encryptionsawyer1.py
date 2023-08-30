import re
import math
import random

def convert_to_binary(data):
    if isinstance(data, int):
        binary_representation = bin(data)[2:]  # Remove '0b' prefix
    elif isinstance(data, float):
        raise ValueError("Cannot convert float to binary directly")
    elif isinstance(data, str):
        binary_representation = ''.join(format(ord(char), '08b') for char in data)
    else:
        raise ValueError("Unsupported data type")
    
    return binary_representation

def convert_binary_to_int(binary_str):
    try:
        decimal_value = int(binary_str, 2)
        return decimal_value
    except ValueError:
        raise ValueError("Invalid binary input")

def count_ones_and_zeros(binary_string):
    ones_count = binary_string.count('1')
    zeros_count = binary_string.count('0')
    return ones_count, zeros_count

def main():
    print("Select an option:")
    print("1. Enter data to convert to binary and integer")
    print("2. Enter a file path to convert its contents to binary and integer")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        input_data = input("Enter data to convert: ")
        try:
            binary_data = convert_to_binary(input_data)
            integer_output = convert_binary_to_int(binary_data)
            print("Binary representation:", binary_data)
            print("Integer value:", integer_output)
            
            # Assign values to variables
            binary_value = binary_data
            integer_value = integer_output
        except ValueError as e:
            print("Error:", e)
    elif choice == '2':
        file_path = input("Enter file path: ")
        try:
            with open(file_path, 'r') as file:
                file_contents = file.read()
                binary_data = convert_to_binary(file_contents)
                integer_output = convert_binary_to_int(binary_data)
                print("Binary representation:", binary_data)
                print("Integer value:", integer_output)
                
                # Assign values to variables
                binary_value = binary_data
                integer_value = integer_output
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Error:", e)
    else:
        print("Invalid choice")

    # Binary and Integer Manipulation
    ones_count, zeros_count = count_ones_and_zeros(binary_value)

    if zeros_count >= 3:
        ones_count **= 3
        zeros_count **= 3

    pin = input("Enter a 4-digit pin (excluding 0): ")
    first_part = pin[:2]
    second_part = pin[2:]

    result = ones_count * zeros_count * int(binary_value, 2)
    
    # Regular expression to find every 3rd numeric character
    numeric_characters = re.findall(r'\d', input_data)
    selected_numeric_characters = numeric_characters[::3]
    
    # Insert characters if the selected number is zero
    for index, char in enumerate(selected_numeric_characters):
        if char == '0':
            random_character = random.choice("!@#$%^&*()_-:; ' , . /?~`")
            result = result[:index] + random_character + result[index:]

    # Calculate encrypted data length
    encrypted_data = str(result)
    encrypted_data_length = len(encrypted_data) * len(binary_value) // 2 * 11
    if encrypted_data_length > 4:
        # Calculate encrypted data length
        encrypted_data = str(result)
        encrypted_data_length = str(len(encrypted_data) * len(binary_value) // 2 * 11)
    if len(encrypted_data_length) > 4:
        encrypted_data_length = encrypted_data_length[:4]

# Combine encrypted data length with pin
        control_number = encrypted_data_length + pin

# Print Encrypted Data and Control Number
    print("Encrypted Data:", encrypted_data)
    print("Control Number:", control_number)


if __name__ == "__main__":
    main()
