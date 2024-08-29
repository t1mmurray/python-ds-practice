def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """



    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!

    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Iterate over each line in the file
            for line in file:
                # Strip leading/trailing whitespace and print the line with a "-"
                print(f"- {line.strip()}")
    except FileNotFoundError:
        print(f"The file at {filename} was not found.")
    except IOError:
        print(f"An error occurred while reading the file at {filename}.")

