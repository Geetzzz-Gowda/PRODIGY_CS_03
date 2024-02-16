#Password complexity checker
import re

def assess_password_strength(password):
    length_score = len(password) // 8  # Assume 8 characters as a baseline
    uppercase_score = 1 if re.search(r'[A-Z]', password) else 0
    lowercase_score = 1 if re.search(r'[a-z]', password) else 0
    digit_score = 1 if re.search(r'\d', password) else 0
    special_char_score = 1 if re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?/~\\-]', password) else 0

    strength_score = length_score + uppercase_score + lowercase_score + digit_score + special_char_score

    if strength_score <= 1:
        return "Weak"
    elif strength_score <= 3:
        return "Moderate"
    elif strength_score <= 5:
        return "Strong"
    else:
        return "Very Strong"

def main():
    password = input("Enter your password: ")
    strength = assess_password_strength(password)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()
