from app.io.input import input_text_from_console, read_from_file, read_from_file_with_pandas
from app.io.output import output_text_to_console, write_to_file


def main():
    # text input
    user_input = input_text_from_console()
    output_text_to_console(user_input)
    write_to_file('from_console.txt', user_input)
    # text file input
    file_content = read_from_file('sample.txt')
    output_text_to_console(file_content)
    write_to_file('from_sample.txt', file_content)

    dataframe = read_from_file_with_pandas('missile_attacks_daily.csv')
    output_text_to_console(str(dataframe))
    write_to_file('from_missiles.txt', str(dataframe))


if __name__ == "__main__":
    main()
