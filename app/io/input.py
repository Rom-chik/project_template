
def input_text_from_console():
    """
    Prompt the user to enter text from the console and return the entered text.

    Returns:
        str: The text entered by the user.
    """
    return input('Enter text: ')

def read_from_file(filename):
    """
    Read the content of the file specified by 'filename' using Python's built-in capabilities and return it as a string.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        str: The content of the file as a string.
    """
    with open(filename, 'r') as file:
        return file.read()

def read_from_file_with_pandas(filename):
    """
        Use the pandas library to read a CSV file specified by 'filename' and return the data as a DataFrame.

        Args:
            filename (str): The name of the file to be read, expected to be in CSV format.

        Returns:
            DataFrame: The data from the CSV file loaded into a pandas DataFrame.
        """
    import pandas as pd
    return pd.read_csv(filename)
