import re

def check_password_strength(password):
    # Initial score and feedback list
    score = 0
    feedback = []
    
    # 1. Length check (Minimum 8 characters)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")
        
    # 2. Uppercase letter check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter (A-Z).")
        
    # 3. Lowercase letter check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter (a-z).")
        
    # 4. Number check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")
        
    # 5. Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (e.g., @, #, $, %, *).")
        
    # Determine strength based on the total score
    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong 👍"
    elif score == 3:
        strength = "Medium 😐"
    else:
        strength = "Weak ❌"
        
    return strength, feedback

def main():
    print("--- Password Strength Checker ---")
    
    while True:
        password = input("\nEnter a password to test (or type 'exit' to quit): ").strip()
        
        if password.lower() == 'exit':
            print("Exiting the program. Thank you!")
            break
            
        if not password:
            print("Password cannot be empty!")
            continue
            
        # Get strength assessment and suggestions
        strength, feedback_list = check_password_strength(password)
        
        print(f"Password Strength: {strength}")
        
        # Display specific recommendations if the password is weak
        if feedback_list:
            print("\nSuggestions for improvement:")
            for item in feedback_list:
                print(f"- {item}")
        else:
            print("Congratulations! Your password is highly secure.")

if __name__ == "__main__":
    main()
