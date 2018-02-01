import sys
import os
import collections


def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as text_file:
        text_list = text_file.read().split()
    return text_list


def get_most_frequent_words(text_list, count_words=10):
    most_frequent_words = collections.Counter(text_list).most_common(count_words)
    return most_frequent_words


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        if os.path.isfile(filepath):
            text_data = load_data(filepath)
            print(get_most_frequent_words(text_data))
        else:
            print("File not found")
    except IndexError:
        print("Arguments error")
    except ValueError:
        print("The specified file format does not match")