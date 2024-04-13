
def input_text_from_console():
    return input('Enter text: ')

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def read_from_file_with_pandas(filename):
    import pandas as pd
    return pd.read_csv(filename)
