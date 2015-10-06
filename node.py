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
