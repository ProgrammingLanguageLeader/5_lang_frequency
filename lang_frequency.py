import argparse
from collections import Counter


def load_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except IOError:
        return None


def delete_special_chars(text):
    for char in text:
        if not char.isalnum():
            text = text.replace(char, ' ')
    return text


def get_most_frequent_words(text, count):
    words_counter = Counter(text.lower().split())
    return [word for word, repeats in words_counter.most_common(count)]


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser(
        description='The script calculates a frequency of words '
                    'in the text and outputs the most popular words'
    )
    argument_parser.add_argument(
        '-i',
        '--input',
        default='',
        help='A path to the file containing text to analyze',
    )
    argument_parser.add_argument(
        '-n',
        '--number',
        type=int,
        default=10,
        help='A number of popular words that will be printed by the program'
    )

    arguments = argument_parser.parse_args()
    input_path = arguments.input
    if not input_path:
        input_path = input('Specify a text file to analyze: ')
    words_number = arguments.number
    if words_number <= 0:
        exit('-n parameter must be positive')

    raw_text = load_text(input_path)
    if not raw_text:
        exit('Check an input file')
    text = delete_special_chars(raw_text)
    the_most_frequent_words = get_most_frequent_words(text, words_number)
    for index, word in enumerate(the_most_frequent_words):
        print('{}. {}'.format(index + 1, word))
