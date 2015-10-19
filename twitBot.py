import sys
from tokenize import *
from dictionary_words_2 import *
from stochastic_sampling import *

# [brian] Usually `import *` is bad form in python.
# One of the best things that distinguishes it from
# ruby is that it's always easy to tell where some
# behavior comes from. If you `import *` you'll
# later have a hard time figuring out which module
# a given function lives in.

if __name__ == '__main__':
    source = open(sys.argv[1]).read()
    tokens = tokenize(source)
    a_dictionary = list_to_dictionary(tokens)
    stochastic_list = new_list(a_dictionary)
    root_node = construct_tree(stochastic_list)
    first_word = random_word(root_node)
