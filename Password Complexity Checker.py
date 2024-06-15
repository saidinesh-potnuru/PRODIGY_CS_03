import re

class PasswordValidator:
    def __init__(self, password):
        self.password = password
        self.rules = [
            "Password must have at least 8 characters.",
            "Password must contain at least one special character.",
            "Password must contain at least one uppercase letter.",
            "Password must contain at least one lowercase letter.",
            "Password must contain at least one numerical digit."
        ]
        self.conditions = [True, True, True, True, True]

    def check_length(self):
        self.conditions[0] = len(self.password) >= 8

    def check_special_characters(self):
        self.conditions[1] = re.search(r'[\W_]', self.password) is not None

    def check_uppercase(self):
        self.conditions[2] = re.search(r'[A-Z]', self.password) is not None

    def check_lowercase(self):
        self.conditions[3] = re.search(r'[a-z]', self.password) is not None

    def check_digit(self):
        self.conditions[4] = re.search(r'[0-9]', self.password) is not None

    def validate_password(self):
        self.check_length()
        self.check_special_characters()
        self.check_uppercase()
        self.check_lowercase()
        self.check_digit()

        strength = sum(1 for condition in self.conditions if condition)
        print(f"Password strength: {strength}/5")

        for i, condition in enumerate(self.conditions):
            if not condition:
                print(f"Error: {self.rules[i]}")

def main():
    password = input("Enter your password: ")
    validator = PasswordValidator(password)
    validator.validate_password()

if __name__ == "__main__":
    main()
