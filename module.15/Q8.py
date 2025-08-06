#  Write a Python program to check the current position of the file cursor using tell().

filename = "sample.txt"
try:
    with open(filename,"r") as file:
        print("cursor psition:",file.tell())
        
        data = file.read(10)
        print(f"\nRead data: {data}")

        print("cursor podition after reading 10 characters:",file.tell())

except FileNotFoundError:
    print(f"Error: file '{filename}'not found.")
except Exception as e:
    print(f"error occurred: {e}")
