import re


def parseText(a_file):
    content = a_file.readlines()
    a_list = []
    final_list = []
    for line in content:
        a_list += line.split()
    while a_list:
        word = a_list.pop()
        word = word.lower()
        word = re.sub('(\[[^\]]*\])', '', word)
        final_list.append(word)
    return final_list


if __name__ == '__main__':
    list_words = []
    with open('steve.txt', encoding='utf-8') as the_file:
        list_words = parseText(the_file)
    print(list_words)
