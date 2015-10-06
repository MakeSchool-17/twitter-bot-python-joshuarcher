import re
import random


class Node:
    def __init__(self, word, val):
        self.word = word
        self.value = val
        self.left_child = None
        self.right_child = None

    def left_child(self):
        return self.left_child

    def right_child(self):
        return self.right_child

    def get_word(self):
        return self.word

    def get_value(self):
        return self.value

    def insert_right(self, newNode):
        self.right_child = newNode

    def insert_left(self, newNode):
        self.left_child = newNode

    def __lt__(self, other):
        return self.value < other.value


def histogram(source_text):
    content = source_text.readlines()
    a_list = []
    a_dictionary = dict()
    for line in content:
        a_list += line.split()
    while a_list:
        word = a_list.pop()
        word = word.lower()
        word = re.sub('[^a-z]+', '', word)
        if word in a_dictionary:
            a_dictionary[word] += 1
        else:
            a_dictionary[word] = 1
    return a_dictionary


def new_list(a_dictionary):
    a_list = []
    for key, value in a_dictionary.items():
        a_list.append(Node(key, value))
    a_list.sort()
    return a_list


def construct_tree(a_list):
    while len(a_list) > 1:
        first = a_list.pop(0)
        second = a_list.pop(0)
        sum = first.get_value() + second.get_value()
        new_node = Node('', sum)
        new_node.insert_left(first)
        new_node.insert_right(second)
        a_list.append(new_node)
        a_list.sort()
    return a_list[0]


def random_word(root_node):
    word = ''
    while word == '':
        num = random.randint(0, 1)
        if num == 0:
            if root_node.left_child is not None:
                root_node = root_node.left_child
        else:
            if root_node.right_child is not None:
                root_node = root_node.right_child
        word = root_node.get_word()
    return word


if __name__ == '__main__':
    with open('woodchuck.txt', encoding='utf-8') as the_file:
        the_dictionary = histogram(the_file)
        print(the_dictionary)
        the_list = new_list(the_dictionary)
        for x in the_list:
            print(x.get_value())
        root_node = construct_tree(the_list)
        print("Hey now.. " + str(root_node.get_value()))
        print(random_word(root_node))
        a_dictionary = dict()
        for i in range(1000000):
            rando_word = random_word(root_node)
            if rando_word in a_dictionary:
                a_dictionary[rando_word] += 1
            else:
                a_dictionary[rando_word] = 1
        print(a_dictionary)
    print("hello world")
