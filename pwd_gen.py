import random
import string

# Define ambiguous chars
AMBIGUOUS_LOWER = 'lo'
AMBIGUOUS_UPPER = 'IO'
AMBIGUOUS_DIGITS = '01'

# String lib char lists
LOWERCASE = ''.join(c for c in string.ascii_lowercase if c not in AMBIGUOUS_LOWER)
UPPERCASE = ''.join(c for c in string.ascii_uppercase if c not in AMBIGUOUS_UPPER)
NUMBERS = ''.join(c for c in string.digits if c not in AMBIGUOUS_DIGITS)
SPECIAL = string.punctuation

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special, special_to_avoid):
    characters = ""
    if use_uppercase:
        characters += UPPERCASE
    if use_lowercase:
        characters += LOWERCASE
    if use_numbers:
        characters += NUMBERS
    if use_special:
        filtered_special = ''.join(c for c in SPECIAL if c not in special_to_avoid)
        characters += filtered_special
    
    if not characters:
        print("You must select at least one character type!")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator Options")
    
    length = int(input("Enter the desired password length: "))
    
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    special_to_avoid = ""
    if use_special:
        special_to_avoid = input(f"Enter special characters to avoid from this set {SPECIAL} (leave blank to include all): ")

    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special, special_to_avoid)
    
    if password:
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
