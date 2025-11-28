def write_file(file_name, file_content):
    # Add .txt automatically when opening the file
    with open(f"{file_name}.txt", "w") as f:
        f.write(file_content)


def append_file(file_name, append_content):
    # Same file, but append instead of write
    with open(f"{file_name}.txt", "a") as f:
        f.write(append_content)


def read_file(file_name):
    # Read content and return it
    try:
        with open(f"{file_name}.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return None
