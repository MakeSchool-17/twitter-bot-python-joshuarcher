import random
import sys
# words_list = sys.argv[1:]
# if len(words_list) == 0:
#     quit()
#
# random.shuffle(words_list)
# string = ""
# for x in words_list:
#     string += (x + " ")
# word = words_list[0]
# to_compare = ""
# count = 0
#
# while to_compare != word:
#     if count == 0:
#         to_compare = input("Guess the first word to be printed!! ")
#     else:
#         to_compare = input("Ehhhhhh try again loser.. ")
#     count += 1
#
# print("Finally!!!")


def randomize(arrayOStrings):
    random.shuffle(arrayOStrings)
    string = ""
    for x in arrayOStrings:
        string += (x + " ")

    word = arrayOStrings[0]
    to_compare = ""
    count = 0

    while to_compare != word:
        if count == 0:
            to_compare = input("Guess the first word to be printed!! ")
        else:
            to_compare = input("Ehhhhhh try again loser.. ")
        count += 1

    print("Finally!!!")

    return string


if __name__ == '__main__':
    words_list = sys.argv[1:]
    if len(words_list) == 0:
        quit()
    string = randomize(words_list)
    print(string)
