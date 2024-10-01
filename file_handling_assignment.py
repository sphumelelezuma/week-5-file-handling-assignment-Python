def create_file():
    """Creates a new text file and writes initial content to it."""
    try:
        # Open a file in write mode
        with open("my_file.txt", 'w') as file:
            # Write three lines of text to the file
            file.write("Hello, this is line 1.\n")
            file.write("Here is line 2, with a number: 42\n")
            file.write("And this is line 3.\n")
        print("File created and initial content written.")
    except (PermissionError, Exception) as e:
        print(f"Error creating the file: {e}")
    finally:
        print("Create file operation completed.")


def read_file():
    """Reads and displays the contents of the text file."""
    try:
        # Open the file in read mode
        with open("my_file.txt", 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except (PermissionError, Exception) as e:
        print(f"Error reading the file: {e}")
    finally:
        print("Read file operation completed.")


def append_to_file():
    """Appends additional lines to the existing text file."""
    try:
        # Open the file in append mode
        with open("my_file.txt", 'a') as file:
            # Append three additional lines of text
            file.write("This is an appended line 1.\n")
            file.write("Appending another line 2, number: 99\n")
            file.write("Finally, this is appended line 3.\n")
        print("Additional lines appended to the file.")
    except (PermissionError, Exception) as e:
        print(f"Error appending to the file: {e}")
    finally:
        print("Append file operation completed.")


if __name__ == "__main__":
    create_file()    # Create the file and write initial content
    read_file()      # Read and display the contents of the file
    append_to_file() # Append additional lines to the file
    read_file()      # Read and display the updated contents of the file
