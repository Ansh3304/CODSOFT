
import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # All character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each set is included
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length
    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    
    return ''.join(password)

def main():
    print("🔐 Welcome to the Password Generator! 🔐")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
    