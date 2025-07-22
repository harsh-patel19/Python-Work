

def decimal_to_hexadecimal(num):
    if num == 0:
        return "0"
    
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    
    while num > 0:
        remainder = num % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        num = num // 16
    
    return hexadecimal

# Input from user
decimal_number = int(input("Enter a decimal number: "))
hex_value = decimal_to_hexadecimal(decimal_number)
print("Hexadecimal equivalent:", hex_value)
