"""
Password Strength Checker
A beginner-friendly project. Uses only Python's built-in tools.
The password is never printed, saved, or sent anywhere.
"""

import getpass  # built into Python; hides what you type
import string   # built into Python; gives us lists of characters


def check_password_strength(password):
    """Look at a password and return a score and a list of tips."""
    score = 0
    tips = []

    # 1. Check the length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        tips.append("Use 12 or more characters for a stronger password.")
    else:
        tips.append("Make your password at least 8 characters long.")

    # 2. Check for uppercase letters (A-Z)
    if any(char in string.ascii_uppercase for char in password):
        score += 1
    else:
        tips.append("Add at least one UPPERCASE letter.")

    # 3. Check for lowercase letters (a-z)
    if any(char in string.ascii_lowercase for char in password):
        score += 1
    else:
        tips.append("Add at least one lowercase letter.")

    # 4. Check for numbers (0-9)
    if any(char in string.digits for char in password):
        score += 1
    else:
        tips.append("Add at least one number.")

    # 5. Check for special characters (!, @, #, $ ...)
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        tips.append("Add at least one special character like ! @ # $ %")

    return score, tips


def get_rating(score):
    """Turn a score (0-6) into a friendly word."""
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    elif score == 5:
        return "Strong"
    else:
        return "Very Strong"


def main():
    print("=== Password Strength Checker ===")
    print("Your typing will be hidden, and your password is never shown or saved.\n")

    # getpass hides the characters as you type them
    password = getpass.getpass("Enter a password to test: ")

    if password == "":
        print("You did not type anything. Please try again.")
        return

    score, tips = check_password_strength(password)

    # Only the result is shown, never the password itself
    print(f"\nScore: {score} out of 6")
    print(f"Rating: {get_rating(score)}")

    if tips:
        print("\nHow to improve:")
        for tip in tips:
            print(f" - {tip}")
    else:
        print("\nGreat job! This password meets every check.")

    # Remove the password from memory as soon as we are done
    del password


# This line makes the program start when you run the file
if __name__ == "__main__":
    main()


