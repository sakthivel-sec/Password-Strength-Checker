import re

def check_password_strength(password):
    """
    Assess the strength of a password based on several criteria:
    - Length of the password
    - Presence of uppercase letters
    - Presence of lowercase letters
    - Presence of numbers
    - Presence of special characters

    :param password: The password string to assess.
    :return: A string indicating the strength of the password.
    """
    # Criteria for password strength
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    # Check the number of criteria met
    criteria_met = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_char_criteria])

    # Provide feedback based on criteria met
    if criteria_met == 5:
        return "Strong password"
    elif criteria_met >= 3:
        return "Moderate password - consider adding more complexity"
    else:
        return "Weak password - consider making it longer and adding different character types"

def get_feedback(password):
    """
    Provide specific feedback on how to improve the password strength.

    :param password: The password string to assess.
    :return: A list of suggestions for improving the password strength.
    """
    suggestions = []
    
    if len(password) < 8:
        suggestions.append("Increase the length to at least 8 characters.")
    if re.search(r'[a-z]', password) is None:
        suggestions.append("Add lowercase letters.")
    if re.search(r'[A-Z]', password) is None:
        suggestions.append("Add uppercase letters.")
    if re.search(r'[0-9]', password) is None:
        suggestions.append("Include numbers.")
    if re.search(r'[\W_]', password) is None:
        suggestions.append("Use special characters (e.g., !, @, #, $, etc.).")
    
    return suggestions


def main():
    """
    Main function to handle user input and assess password strength.
    """
    print("Password Strength Assessment Tool")

    # Get the password from the user
    password = input("Enter your password: ")

    # Assess the password strength
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")

    # Provide feedback if the password is not strong
    if strength != "Strong password":
        feedback = get_feedback(password)
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()
