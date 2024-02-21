import sys

def custom_encryption(input_text, shift_amount):
    result_text = ""
    for char in input_text:
        if char.isalpha():
            char = char.upper()
            encrypted_char = chr((ord(char) - 65 + shift_amount) % 26 + 65)
            result_text += encrypted_char
    return result_text

def display_encrypted_blocks(text):
    for i in range(0, len(text), 5):
        print(text[i:i+5], end=' ')
    print()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 custom_encryption.py <shift>")
        sys.exit(1)

    try:
        shift = int(sys.argv[1])
        shift = shift % 26
    except ValueError:
        print("Please provide a valid integer for the shift value.")
        sys.exit(1)

    for line in sys.stdin:
        line = line.upper()
        encrypted_message = custom_encryption(line, shift)
        display_encrypted_blocks(encrypted_message)

if __name__ == "__main__":
    main()