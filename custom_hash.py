class LinkedList:
    class Item:
        def __init__(self, word, val):
            self.word = word
            self.val = val
            self.next_item = None

    def __init__(self):
        self.head = None
        self.num_items = 0

    def print_list(self):
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
            return True
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
            return False

    def append_value(self, word, value):
        if self.head is None:
            self.head = LinkedList.Item(word, value)
            self.num_items = self.num_items + 1
        else:
            current_node = self.head
            previous_node = None
            while current_node is not None:
                previous_node = current_node
                current_node = current_node.next_item
            new_node = LinkedList.Item(word, value)
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


class CustomHashTable:

    def __init__(self, buckets):
        self.buckets = [LinkedList() for _ in range(buckets)]
        # list comprehension
        self.num_buckets = buckets
        self.num_items = 0

    def item_count(self):
        return self.num_items

    def add_key_value(self, word, value):
        bucket = hash(word) % self.num_buckets
        self.buckets[bucket].append_value(word, value)
        self.num_items = self.num_items + 1

    def add(self, word):
        loading = self.load_factor()
        if loading > 0.67:
            new_hash_table = CustomHashTable(self.num_buckets * 2)
            for list_things in self.buckets:
                head_list = list_things.head
                while head_list is not None:
                    new_hash_table.add_key_value(head_list.word, head_list.val)
                    head_list = head_list.next_item
            self.buckets = new_hash_table.buckets
            self.num_buckets = new_hash_table.num_buckets
            self.num_items = new_hash_table.num_items
        bucket = hash(word) % self.num_buckets
        if self.buckets[bucket].append(word) is True:
            self.num_items = self.num_items + 1

    def print_hash(self):
        for i in range(self.num_buckets):
            print("---")
            self.buckets[i].print_list()

    def load_factor(self):
        return self.num_items / self.num_buckets


if __name__ == '__main__':
    words = ["josh", "word", "tyler", "nick", "captain", "dan", "isabel", "adrian", "mike", "kalson", "connor", "hunter"]
    hashTable = CustomHashTable(10)
    for word in words:
        hashTable.add(word)
    for word in words:
        hashTable.add(word)
    hashTable.print_hash()
    print(hashTable.num_buckets)
