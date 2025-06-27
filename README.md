# My Toolkit 📦

A simple Python utility package offering:

- Temperature conversion functions
- Basic math operations
- String utilities

---

## 🛠️ Installation

# Clone the repo
git clone https://github.com/dkishorkoirala/My_toolkit.git

# (Optional) Install via pip
pip install git+https://github.com/dkishorkoirala/My_toolkit.git


📦 Package Structure
markdown
my_toolkit/
│
├── __init__.py
├── temp_converter.py
├── math_ops.py
└── string_utils.py

🔧 Usage Example
from my_toolkit import (
    to_celsius, to_fahrenheit,
    mul, div,
    count_words, is_palindrome
)

print(to_celsius(100))     # → 37.78
print(to_fahrenheit(0))    # → 32.0

print(mul(4, 5))           # → 20
print(div(10, 2))          # → 5.0

sentence = "Hello world from Toolkit"
print(count_words(sentence))  # → 4

print(is_palindrome("radar")) # → YES the word is palindrome

🧪 Function Details
Function	Description
to_celsius(f)	Converts Fahrenheit to Celsius
to_fahrenheit(c)	Converts Celsius to Fahrenheit
mul(a, b)	Returns product
div(a, b)	Returns quotient (handles divide-by-zero)
count_words(text)	Returns the number of words in text
is_palindrome(s)	Checks if s is a palindrome (case-sensitive)

🤝 Contributing
Feel free to:

Open issues 🔍

Send pull requests 🛠️

Discuss feature ideas in Issues

📄 License
This project is licensed under the MIT License. See LICENSE for details.
