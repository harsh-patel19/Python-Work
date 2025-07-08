# Get input from user
decimal = int(input("Enter a decimal number: "))

# Initialize binary string
binary = ""

# Check if the number is 0
if decimal == 0:
    binary = "0"
else:
    while decimal > 0:
        remainder = decimal % 2           # Get remainder (0 or 1)
        binary = str(remainder) + binary  # Add to the left side of binary string
        decimal = decimal // 2            # Reduce the number by dividing by 2

# Print binary output
print("Binary equivalent is:", binary)

