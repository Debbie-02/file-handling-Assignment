def file_read_write():
    try:
        # Ask user for filename
        filename = input("Enter the filename to read: ")
        
        # Open and read the file
        with open(filename, "r") as f:
            content = f.read()
        
        # Modify the content (example: make all text uppercase)
        modified_content = content.upper()
        
        # Create a new file to write modified content
        new_filename = "modified_" + filename
        with open(new_filename, "w") as f:
            f.write(modified_content)
        
        print(f"File has been successfully read and modified content written to '{new_filename}'")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the function
file_read_write()