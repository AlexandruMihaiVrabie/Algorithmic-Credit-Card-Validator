def verify_card_number(string):
    digits = []

    for char in string:
        if char.isdigit():
            digits.append(int(char))

    for i in range(len(digits) - 2, -1, -2):
        doubled_digit = digits[i] * 2

        if doubled_digit > 9:
            digits[i] = doubled_digit - 9
        else:
            digits[i] = doubled_digit

    if sum(digits) % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"


print(verify_card_number("453914889"))
print(verify_card_number("4111-1111-1111-1111"))
print(verify_card_number("1234 5678 9012 3456"))
