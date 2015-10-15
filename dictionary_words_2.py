

def list_to_dictionary(list):
    a_dictionary = dict()
    for word in list:
        if word in a_dictionary:
            a_dictionary[word] += 1
        else:
            a_dictionary[word] = 1
    return a_dictionary


if __name__ == '__main__':
    from tokenize import *
    import sys
    source = open(sys.argv[1]).read()
    tokens = tokenize(source)
    dictionary = list_to_dictionary(tokens)
    #print(dictionary)
    for word, frequency in dictionary.items():
        print("{}: {}".format(word, frequency))
