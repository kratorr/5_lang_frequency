import sys
import os
import collections
import re


def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as text_file:
        text_string = text_file.read()
    return text_string


def clean_text(text_string):
    pattern = r"[\W0-9_]"
    clean_text_string = re.sub(pattern, " ", text_string)
    return clean_text_string


def text_to_list(text_string):
    text_list = text_string.split()
    return text_list


def get_most_frequent_words(text_list, quantity_words=10):
    most_frequent_words = collections.Counter(text_list).most_common(quantity_words)
    return most_frequent_words


def print_most_frequent_words(most_frequent_words):
    print("10 most frequent words in the text: ")
    for words in most_frequent_words:
        print('"{}" - quantity: {}'.format(*words))


if __name__ == "__main__":
    try:
        filepath = sys.argv[1]
        if os.path.isfile(filepath):
            clean_text = clean_text(load_data(filepath))
            words_list  = text_to_list(clean_text)
            print_most_frequent_words(get_most_frequent_words(words_list ))
        else:
            print("File not found")
    except IndexError:
        print("Arguments error")
    except ValueError:
        print("The specified file format does not match")
