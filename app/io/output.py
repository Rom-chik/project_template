
def output_text_to_console(text):
    """
        Output the text specified by 'text' to the console.

        Args:
            text (str): The text to be output.

        Returns:
            None
        """
    print(text)

def write_to_file(filename, text):
    """
        Write the text specified by 'text' to a file named 'filename' using Python's built-in capabilities.

        Args:
            filename (str): The name of the file where the text will be written.
            text (str): The text to write to the file.

        Returns:
            None
        """
    with open(filename, 'w') as file:
        file.write(text)
