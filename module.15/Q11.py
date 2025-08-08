# Write a Python program to handle file exceptions and use the finally block for closing
#the file.


def read_file_content(filename):
    file = None
    try:
        file.open(filename,'r')
        content = file.read()
        print(content)
    except SyntaxError as e:
         print(e)
    except AttributeError as e:
        print(e)
    except Exception as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except TypeError as e:
        print(e)
    finally:
        if file:
            file.close()
            print(f"has been closed{filename}.")
        else:
            print("open the file")
filename = input("Enter the filename to read: ")
read_file_content(filename)