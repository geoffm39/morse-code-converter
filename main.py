from codes import code_library
from art import logo

#  create a function for converting text to morse code
    # invalid symbols are converted to a #
    # split by word, then by character (nested lists)
    # convert multiple spaces into multiple ///
        # check for '' in list. converts to an extra space #### DIDNT NEED TO DO!
    # use '/'.join() and ' '.join() to join the lists back into strings

def convert__to_code(text):
    split_text = [[char.lower() for char in word] for word in text.split(' ')]

    for word in split_text:
        for index, char in enumerate(word):
            if char in code_library:
                word[index] = code_library[char]
            else:
                word[index] = '#'

    converted_words = [' '.join(word) for word in split_text]
    converted_text = ' / '.join(converted_words)

    return converted_text

# create a function for converting morse code to text
    # invalid codes are converted to a #
    # divide string into lists of words, then again into lists of characters
    # grammar: set first letter of sentance to a capitol letter, and double space after full stop
    # must represent a space, no matter how many in a row
        #  check '' and ' ' after split
def convert_to_text(coded_text):
    split_code = [[char_code for char_code in word.split()] for word in coded_text.split('/')]

    for coded_word in split_code:
        for index, code in enumerate(coded_word):
            if code not in code_library.values():
                coded_word[index] = '#'
            else:
                for key, value in code_library.items():
                    if code == value:
                        coded_word[index] = key

    converted_code_words = [''.join(coded_word) for coded_word in split_code]

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

    converted_code = ' '.join(converted_code_words)

    return converted_code


#  create converter function that runs the converter until user is finished
    #  ask what type of conversion to execute
    #  call the correct function based on input and return the printed result
    # ask user if wants to continue. use recursion to loop back to start if continuing


def converter():
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
    print(logo)
    print('Welcome to the Morse Code Converter')
    converter()


if __name__ == '__main__':
    main()
