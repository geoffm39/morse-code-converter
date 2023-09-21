from codes import code_library
from art import logo

# TODO: create a function for converting text to morse code
    # TODO: invalid symbols are converted to a #
    # TODO: split by word, then by character (nested lists)
    # TODO: convert multiple spaces into multiple ///
        # TODO: check for '' in list. converts to an extra space
    # TODO: use '/'.join() and ' '.join() to join the lists back into strings

def convert_text(text):
    split_sentences = text.split(' ')


# TODO: create a function for converting morse code to text
    # TODO: invalid codes are converted to a #
    # TODO: divide string into lists of words, then again into lists of characters
    # TODO: grammar: set first letter of sentance to a capitol letter, and double space after full stop
    # TODO: / must represent a space, no matter how many in a row
        # TODO: check '' and ' ' after split

# TODO: create converter function that runs the converter until user is finished
    # TODO: ask what type of conversion to execute
    # TODO: call the correct function based on input and return the printed result
    # TODO: ask user if wants to continue. use recursion to loop back to start if continuing

