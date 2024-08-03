def check_password_strength(password):
    """
    Checks the strength of a password.
    Args:
        password (str): The password to evaluate.
    Returns:
        str: Feedback on password strength.
    """
    length_ok = len(password) >= 8
    uppercase_ok = any(c.isupper() for c in password)
    lowercase_ok = any(c.islower() for c in password)
    digit_ok = any(c.isdigit() for c in password)
    special_char_ok = any(c in "!@#$%^&*()_+[]{}|;:,.<>?~" for c in password)

    if length_ok and uppercase_ok and lowercase_ok and digit_ok and special_char_ok:
        return "Strong password! 🌟"
    elif length_ok and (uppercase_ok or lowercase_ok) and digit_ok:
        return "Moderate password. Consider adding special characters."
    else:
        return "Weak password. Aim for longer length and more complexity."

# Example usage:
user_password = input("Enter a password: ")
strength_feedback = check_password_strength(user_password)
print(strength_feedback)
