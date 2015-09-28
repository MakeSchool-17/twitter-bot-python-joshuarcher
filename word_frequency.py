import re
import time


def histogram(source_text):
    content = source_text.readlines()
    a_list = []
    a_dictionary = dict()
    for line in content:
        a_list += line.split()
    while a_list:
        word = a_list.pop()
        word = word.lower()
        word = re.sub('[^0-9a-z]+', '', word)
        if word in a_dictionary:
            a_dictionary[word] += 1
        else:
            a_dictionary[word] = 1
    return a_dictionary


def unique_words(a_dictionary):
    return len(a_dictionary)


def frequency(a_word, a_dictionary):
    return a_dictionary[a_word]

if __name__ == '__main__':
    start_time = time.time()
    with open('comp_network.txt', encoding='utf-8') as the_file:
        the_dictionary = histogram(the_file)
        print(unique_words(the_dictionary))
        print(frequency("people", the_dictionary))
    print("--- %s seconds ---" % (time.time() - start_time))
