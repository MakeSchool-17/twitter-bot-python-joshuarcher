import random
import sys


def wow(list, num):
    a_string = ""
    new_list = random.sample(list, num)
    while len(new_list) > 0:
        word = new_list.pop()
        a_string += (word[:-1] + " ")
    print(a_string)

if __name__ == '__main__':
    num_words = sys.argv[1:]
    int_words = 0
    if len(num_words) == 1:
        int_words = int(num_words[0])
    else:
        quit()
    with open('/usr/share/dict/words', encoding='utf-8') as the_file:
        a_list = the_file.readlines()
        wow(a_list, int_words)
        print("Finsihed")

# takes in a number
#     the number is how many words to return
# picks number words randomly
#     for each one get rid of the \n
# returns string of words without the \n
#
#
#
#
#
#
