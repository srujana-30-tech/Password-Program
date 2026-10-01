# Password Strength Checker

## Description
This Python program checks the strength of a password using Object-Oriented Programming (OOP). It verifies whether the password contains at least 8 characters, a digit, and an uppercase letter.

## Features
- Accepts a password from the user.
- Checks the password length.
- Checks for at least one digit.
- Checks for at least one uppercase letter.
- Displays either `Strong` or `Weak`.

## Concepts Used
- Python Classes and Objects
- Constructor (`__init__`)
- Methods
- Conditional Statements
- `for` Loop
- String Methods
  - `isdigit()`
  - `isupper()`
- User Input

## Password Strength Conditions

A password is considered **Strong** when all three conditions are satisfied:

1. Password length is at least 8 characters.
2. Password contains at least one digit.
3. Password contains at least one uppercase letter.

Otherwise, the password is considered **Weak**.

## Program Code

```python
class Password:
    def __init__(self, password):
        self.password = password

    def check_strength(self):
        digit = False
        upper = False

        for ch in self.password:
            if ch.isdigit():
                digit = True
            if ch.isupper():
                upper = True

        if len(self.password) >= 8 and digit and upper:
            print("Strong")
        else:
            print("Weak")


paswd = input("Enter password: ")
p = Password(paswd)
p.check_strength()
