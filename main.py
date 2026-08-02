import secrets

def display_welcome_message():
    print("=" * 45)
    print()
    print("Welcome to the Password Generator!")
    print()
    print("=" * 45)
    print()

def get_password_length():
    while True:
        length = input("Enter desired password length (8-32): ")
        if length.isdigit():
            length = int(length)
            if 8 <= length <= 32:
                return length
        print("Error: Please enter a valid password length (8-32).")

def get_yes_no_choice(prompt):
    while True:
        choice = input(prompt).strip().lower()

        if choice in ("y", "yes"):
            return True
        elif choice in ("n", "no"):
            return False

        print("Error: Please enter 'y'/'yes' or 'n'/'no'.")

def build_character_pool(include_lowercase, include_uppercase, include_digits, include_special):
    lowercase = "abcdefghijklmnopqrstuvwxyz" if include_lowercase else ""
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if include_uppercase else ""
    digits = "0123456789" if include_digits else ""
    special = "!@#$%^&*()-+" if include_special else ""
    return lowercase + uppercase + digits + special

def generate_password(length, character_pool):
    return ''.join(secrets.choice(character_pool) for _ in range(length))

def display_generated_password(password):
        print(f"Generated Password: {password}")
        print()

def ask_to_continue():
    continue_choice = get_yes_no_choice(
        "Do you want to generate another password? (y/n): "
    )
    print()

    if continue_choice:
        return True

    print("Exiting the Password Generator. Goodbye!")
    return False

def run_password_generator():
    display_welcome_message()

    want_to_continue = True
    while want_to_continue:

        # Get length
        length  = get_password_length()
        print()

        # Get character types
        include_lowercase = get_yes_no_choice("Include lowercase letters? (y/n): ")
        include_uppercase = get_yes_no_choice("Include uppercase letters? (y/n): ")
        include_digits    = get_yes_no_choice("Include digits? (y/n): ")
        include_special   = get_yes_no_choice("Include special characters? (y/n): ")
        print()

        # Validate character type selection
        if not any([include_lowercase, include_uppercase, include_digits, include_special]):
            print("Error: At least one character type must be selected.")
            print()
            continue

        # Build character pool
        character_pool = build_character_pool(
            include_lowercase = include_lowercase,
            include_uppercase = include_uppercase,
            include_digits    = include_digits,
            include_special   = include_special
        )

        # Generate password
        password = generate_password(length, character_pool)

        # Display generated password
        display_generated_password(password)

        # Ask if the user wants to generate another password
        want_to_continue = ask_to_continue()

if __name__ == "__main__":
    run_password_generator()