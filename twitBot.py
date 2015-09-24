import random
import sys

words_list = sys.argv[1:]
if len(words_list) == 0:
    quit()


random.shuffle(words_list)
string = ""
for x in words_list:
    string += (x + " ")

print(string)
