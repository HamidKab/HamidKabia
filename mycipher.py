import sys

def encrypt_text(input_text, shift_amount):
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
        print("Please give a secret number as a command line argument.")
        sys.exit(1)

    try:
        secret_number = int(sys.argv[1])
        secret_number = secret_number % 26
    except ValueError:
        print("Please enter a valid whole number for the secret number.")
        sys.exit(1)

    
    for line in sys.stdin:
        line = line.upper()
        encrypted_message = encrypt_text(line, secret_number)
        
        display_encrypted_blocks(encrypted_message)

if __name__ == "__main__":
    main()
