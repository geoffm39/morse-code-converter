from codes import code_library
from art import logo


def convert__to_code(text: str):
    """
    Convert text to morse code.
    :param text: (str): The text to convert to morse code.
    :return: (str): The converted morse code.
    """
    # split characters into nested lists
    split_text = [[char.lower() for char in word] for word in text.split(' ')]

    # convert characters to codes
    for word in split_text:
        for index, char in enumerate(word):
            if char in code_library:
                word[index] = code_library[char]
            else:
                word[index] = '#'

    # join lists into one string
    converted_words = [' '.join(word) for word in split_text]
    converted_text = ' / '.join(converted_words)

    return converted_text


def convert_to_text(coded_text: str):
    """
    Convert morse code to formatted text with spaced sentences and capital letters.
    :param coded_text: (str): The morse code to convert to text.
    :return: (str): The converted text.
    """
    # split coded into nested lists
    split_code = [[char_code for char_code in word.split()] for word in coded_text.split('/')]

    # convert codes to characters
    for coded_word in split_code:
        for index, code in enumerate(coded_word):
            if code not in code_library.values():
                coded_word[index] = '#'
            else:
                for key, value in code_library.items():
                    if code == value:
                        coded_word[index] = key

    # join characters into words
    converted_code_words = [''.join(coded_word) for coded_word in split_code]

    # Text formatting
    next_word_capital = True
    for index, word in enumerate(converted_code_words):
        if next_word_capital:
            if word:
                converted_code_words[index] = word.capitalize()
                next_word_capital = False
        if word:
            if word[-1] == '.':
                converted_code_words[index] += ' '
                next_word_capital = True

    # join words into one string
    converted_code = ' '.join(converted_code_words)

    return converted_code


def converter():
    """
    Ask for user input and run relevant code.
    :return: None
    """
    command = input("Enter 't' to convert to text, or 'c' to convert to code: ").lower()
    if command == 't':
        text = convert_to_text(input("Enter the morse code to convert:\n"))
        print(f"The converted morse code is:\n{text}\n")
    elif command == 'c':
        code = convert__to_code(input("Enter the text to convert:\n"))
        print(f"The converted text is:\n{code}\n")
    else:
        print("You entered an invalid command.  Please try again.")
        converter()

    if input("Would you like to convert something else? y/n ").lower() == 'y':
        converter()
    else:
        print("\nThanks for using the Morse Code Converter. Feedback is welcome!")


def main():
    """
    Main function.
    :return: None
    """
    print(logo)
    print('Welcome to the Morse Code Converter')
    converter()


if __name__ == '__main__':
    main()
