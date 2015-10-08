class LinkedList:
    class Item:
        def __init__(self, word, val):
            self.word = word
            self.val = val
            self.next_item = None

    def __init__(self):
        self.head = None
        self.num_items = 0

    def printList(self):
        print("Showing list data: ")
        current_node = self.head
        while current_node is not None:
            print("({}, {}) -> ".format(current_node.word, current_node.val))
            current_node = current_node.next_item
        print(None)

    def append(self, word):
        if self.head is None:
            self.head = LinkedList.Item(word, 1)
            self.num_items = self.num_items + 1
        else:
            current_node = self.head
            previous_node = None
            while current_node is not None:
                if current_node.word is word:
                    current_node.val = current_node.val + 1
                    return
                previous_node = current_node
                current_node = current_node.next_item
            new_node = LinkedList.Item(word, 1)
            previous_node.next_item = new_node
            self.num_items = self.num_items + 1

    def remove(self, word):
        if self.head is None:
            return
        else:
            current_node = self.head
            previous_node = None
            while current_node.word is not None:
                if current_node.word is word:
                    if previous_node is not None:
                        previous_node.next_item = current_node.next_item
                    else:
                        self.head = current_node.next_item
                previous_node = current_node
                current_node = current_node.next_item

    def size(self):
        return self.num_items
