# Credit Card Validator (Luhn Algorithm)

A simple, robust, and efficient Python script for validating credit card numbers. This project implements the **Luhn Algorithm** (also known as the *Modulus 10* algorithm), a widely used checksum formula to validate a variety of identification numbers, especially bank card numbers, to prevent accidental typing errors.

## 🚀 Features

* **Flexible Input Processing:** The `verify_card_number` function automatically filters out non-numeric characters. Whether the card number is entered as a continuous string (`4111111111111111`), separated by spaces (`1234 5678 9012 3456`), or delimited by dashes (`4111-1111-1111-1111`), the script will accurately extract and process only the digits.
* **Zero Dependencies:** The code is written entirely using built-in Python features. No external packages or libraries are required.
* **Fast Evaluation:** It utilizes basic mathematical operations and native data structures to instantly return a clear verdict (`VALID!` or `INVALID!`).

## 🧠 How the Luhn Algorithm Works Here

To determine if a number is valid, the script follows these logical steps directly on the list of extracted digits:
1. Iterates through the list of digits from right to left.
2. Doubles the value of every second digit, starting from the second-to-last one.
3. If the doubled value is greater than 9, it subtracts 9 from the result (this is mathematically equivalent to adding the digits of the product together, e.g., `7 * 2 = 14`, and `14 - 9 = 5`).
4. Sums up all the digits (both the doubled/adjusted ones and the untouched ones).
5. If the total sum is perfectly divisible by 10 (i.e., `sum % 10 == 0`), the card number is **VALID!**.

## 🛠️ Requirements & Running

This project only requires **Python 3.x** installed on your system.

1. Clone this repository or download the `credit_card_validator.py` file.
2. Open a terminal or command prompt.
3. Navigate to the folder containing the file and run the following command:

```bash
python credit_card_validator.py
```

## 💻 Code Example & Usage

You can use this script either by running it directly or by importing the function into your own project:

```python
# Function call examples

print(verify_card_number("453914889"))             # Random test number
print(verify_card_number("4111-1111-1111-1111"))   # Dashed format
print(verify_card_number("1234 5678 9012 3456"))   # Spaced format
```

**Expected Output:**
```text
INVALID!
VALID!
INVALID!
```

## 🤝 Contributing

Contributions are always welcome! If you have ideas to extend this script (for example, adding support to identify the card issuer like Visa, Mastercard, American Express based on the prefix), feel free to fork this repository and open a Pull Request.
