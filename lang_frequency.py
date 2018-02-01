import sys
import os


def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as text_file:
        text_list = [i.split() for i in text_file if len(i.split()) != 0]
        return text_list


def get_most_frequent_words(text, count_words=10):
    words_dict = {}
    for lines in text:
        for word in lines:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

    sorted_list = sorted(words_dict.items(), key=lambda item: item[1], reverse=True)
    most_frequent_words = []
    for i in range(count_words):
        most_frequent_words.append(sorted_list[i][0])
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