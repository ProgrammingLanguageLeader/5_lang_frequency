import argparse
import string


def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = file.read()
        return data
    except IOError:
        return None


def delete_special_chars(text):
    special_chars_string = string.punctuation
    for char in special_chars_string:
        text = text.replace(char, '')
    return text


def get_most_frequent_words(text, count):
    words_from_text = {}
    for word in text.split():
        if words_from_text.get(word.lower()):
            words_from_text[word.lower()] += 1
        else:
            words_from_text[word.lower()] = 1
    the_most_frequent_words = sorted(
        words_from_text,
        key=words_from_text.get,
        reverse=True
    )[:count]
    return the_most_frequent_words


def print_the_most_frequent_words(words_list):
    for index, word in enumerate(words_list):
        print(' {}. {}'.format(index + 1, word))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='The script calculates a frequency of words '
                    'in the text and outputs the most popular words'
    )
    parser.add_argument(
        '-i',
        '--input',
        default='',
        help='A path to the file containing text to analyze',
    )
    parser.add_argument(
        '-n',
        '--number',
        type=int,
        default=10,
        help='A number of popular words that will be printed by the program'
    )

    args = parser.parse_args()
    input_path = args.input
    if input_path == '':
        input_path = input('Specify a text file to analyze: ')
    words_number = args.number
    if words_number <= 0:
        print('-n parameter must be positive')
        exit(0)

    raw_text = load_data(input_path)
    if not raw_text:
        print('Check an input file')
        exit(0)
    text = delete_special_chars(raw_text)
    the_most_frequent_words = get_most_frequent_words(text, words_number)
    print_the_most_frequent_words(the_most_frequent_words)
