# 🔐 Password Generator

A secure, modular command-line Password Generator built with Python that allows users to generate customizable passwords based on configurable security requirements.

The application uses Python's `secrets` module to generate cryptographically secure random passwords and demonstrates clean software architecture through modular design, reusable helper functions, input validation, and configuration-driven application flow.

---

# 📌 Project Overview

The Password Generator enables users to generate secure passwords by selecting the desired password length and the character categories to include.

Rather than generating a fixed password format, the application dynamically constructs a character pool based on user preferences before securely generating a password using cryptographically secure randomness.

The project emphasizes modular software design, reusable functions, defensive programming, and separation of responsibilities while introducing secure random number generation using Python's standard library.

---

# ✨ Features

* Configurable password length
* Secure password generation using the `secrets` module
* Support for:

  * Lowercase letters
  * Uppercase letters
  * Numbers
  * Special characters
* User input validation
* Menu-driven interaction
* Generate multiple passwords without restarting the application
* Clean modular architecture
* Reusable helper functions

---

# 🛠 Technologies Used

* Python 3
* Python Standard Library

  * `secrets`

No external libraries are required.

---

# 📂 Project Structure

```text
Password-Generator/
│
├── main.py
├── README.md
├── LICENSE
└── .gitignore
```

---

# ⚙️ Application Workflow

```text
Start Application
        │
        ▼
Display Welcome Message
        │
        ▼
Choose Password Length
        │
        ▼
Choose Character Types
        │
        ▼
Validate User Selections
        │
        ▼
Build Character Pool
        │
        ▼
Generate Password
        │
        ▼
Display Password
        │
        ▼
Generate Another?
        │
   ┌────┴────┐
   │         │
  Yes       No
   │         │
   ▼         ▼
Repeat     Exit
```

---

# 🔑 Password Configuration

The application allows users to configure the password by selecting:

* Password Length
* Include Lowercase Letters
* Include Uppercase Letters
* Include Numbers
* Include Special Characters

The password is then generated using only the selected character categories.

---

# 🔒 Secure Password Generation

Unlike many beginner implementations that rely on Python's `random` module, this project uses the `secrets` module.

```python
import secrets
```

The `secrets` module is specifically designed for security-sensitive applications such as:

* Password generation
* Authentication tokens
* Cryptographic keys
* Session identifiers

This makes the generated passwords significantly more suitable for real-world usage.

---

# 🧩 Character Pool Construction

The application dynamically builds the available character pool based on the user's selections.

Example:

If the user selects:

* Lowercase
* Numbers

The resulting character pool becomes:

```text
abcdefghijklmnopqrstuvwxyz0123456789
```

If all categories are selected, the pool contains:

* Lowercase letters
* Uppercase letters
* Digits
* Special characters

This configuration-driven approach keeps the generator flexible and easy to extend.

---

# ✅ Input Validation

The application validates several types of user input.

### Password Length

The password length must fall within the allowed range.

Invalid values include:

* Text input
* Negative values
* Values below the minimum
* Values above the maximum

---

### Yes / No Responses

Supported responses include:

```text
y
yes
n
no
```

Invalid responses continue prompting until a valid answer is entered.

---

### Character Selection

The application ensures that at least one character category is selected before generating a password.

This prevents invalid password generation attempts.

---

# 🏗 Software Design

The application follows a modular architecture where each function performs a single responsibility.

Examples include:

* Displaying the welcome message
* Obtaining the password length
* Validating Yes/No responses
* Constructing the character pool
* Generating the password
* Displaying the generated password
* Handling replay logic
* Controlling overall program execution

This separation improves readability, maintainability, testing, and future extensibility.

---

# 💡 Python Concepts Demonstrated

* Functions
* Parameters
* Return values
* Strings
* Loops
* Conditional statements
* Boolean logic
* Input validation
* String concatenation
* Modular programming
* Defensive programming
* Secure random generation
* Program flow

---

# 📈 Software Engineering Concepts Practiced

This project demonstrates practical implementation of:

* Configuration-driven software
* Clean Architecture
* Separation of Responsibilities
* Reusable helper functions
* User input validation
* Defensive programming
* Secure software practices
* Command-line application design
* Modular development
* Maintainable code

---

# 🚀 Possible Future Improvements

The current project provides a strong foundation for a password generator, but it can be expanded into a significantly more advanced security application.

Potential enhancements include:

## Password Complexity Enforcement

Guarantee that generated passwords contain at least one character from every selected category.

Example:

* At least one uppercase letter
* At least one lowercase letter
* At least one number
* At least one special character

---

## Password Strength Analysis

Evaluate generated passwords using metrics such as:

* Entropy
* Character diversity
* Dictionary word detection
* Common password detection
* Estimated crack time

Display an overall strength rating:

* Weak
* Fair
* Strong
* Very Strong

---

## Ambiguous Character Filtering

Allow users to exclude confusing characters such as:

```text
O
0
I
l
1
```

This improves readability while maintaining security.

---

## Custom Character Sets

Allow users to specify their own allowed characters.

Example:

```text
Allowed characters:

ABC123!@
```

---

## Passphrase Generator

Generate memorable passphrases using random dictionary words.

Example:

```text
river-horse-purple-coffee
```

---

## Multiple Password Generation

Generate multiple passwords in one operation.

Example:

```text
Generate 20 passwords
```

---

## Password History

Maintain a history of previously generated passwords during the current session.

---

## Save Passwords Securely

Allow generated passwords to be saved in encrypted files.

---

## Clipboard Integration

Automatically copy generated passwords to the system clipboard.

---

## Password Templates

Generate passwords optimized for different scenarios:

* Banking
* Social Media
* Wi-Fi
* Enterprise Systems
* Developers

---

## Pronounceable Passwords

Generate passwords that remain secure while being easier to remember.

---

## Secure Password Manager

Expand the application into a complete password management system supporting:

* Account storage
* Website categorization
* Encrypted vault
* Master password authentication
* Automatic password generation
* Password search
* Secure backups

---

## Graphical User Interface

Develop a desktop application using:

* Tkinter
* PyQt

---

## Web Version

Build a browser-based password generator using:

* Flask
* FastAPI
* Django

---

## API Version

Expose password generation through a REST API for integration with other systems.

---

## Cloud Synchronization

Synchronize encrypted password vaults across multiple devices.

---

## Biometric Authentication

Integrate fingerprint or facial recognition for accessing stored credentials.

---

# ▶️ Running the Project

Clone the repository:

```bash
git clone https://github.com/yourusername/password-generator.git
```

Navigate to the project directory:

```bash
cd password-generator
```

Run the application:

```bash
python main.py
```

---

# 📊 Skills Demonstrated

* Python Programming
* Secure Random Number Generation
* Modular Programming
* Software Architecture
* Input Validation
* Defensive Programming
* Configuration-Driven Design
* Command-Line Application Development
* Clean Code Principles
* Problem Solving

---

# 📄 License

This project is a personal project

---

# ⭐ Acknowledgements

This project was developed as part of a structured software engineering portfolio focused on building progressively more advanced applications. It emphasizes secure programming practices, modular software architecture, reusable components, and maintainable code while demonstrating the implementation of a configurable command-line password generator using Python's standard library.
