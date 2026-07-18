# Password Strength Checker

A simple and interactive Python program that assesses the strength of a given password based on standard security criteria. It provides real-time feedback and constructive suggestions to help users create more secure passwords.

## Features
- **Strength Evaluation**: Rules-based assessment that rates passwords into four tiers: *Weak*, *Medium*, *Strong*, or *Very Strong*.
- **Criteria Checked**:
  - Minimum length requirement (at least 8 characters).
  - Presence of uppercase letters (`A-Z`).
  - Presence of lowercase letters (`a-z`).
  - Presence of numeric digits (`0-9`).
  - Presence of special characters (e.g., `@`, `#`, `$`, `%`, `*`).
- **Actionable Feedback**: Dynamically generates specific suggestions for any security criteria that the password fails to meet.
- **Interactive Console**: Runs in a continuous loop, allowing users to test multiple passwords until they choose to exit.

## How It Works
The script utilizes Python's built-in regular expressions (`re` module) to efficiently scan the input string for character patterns. Each matching criterion increments a scoring counter, which determines the final strength level.

## Technologies Used
- **Language**: Python 3.x
- **Core Libraries**: Uses standard `re` and `os` modules (no external dependencies required).

## How to Run
1. Ensure you have Python installed on your machine.
2. Clone this repository or download the script file.
3. Run the application via your terminal:
   ```bash
   python password_checker.py
