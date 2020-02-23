import numpy as np
import string
from itertools import compress

def search(index_file, search_string):
    # To be replaced
    x=search_string.lower()
    index_file = open(index_file, 'r')

    doc_list = []
    index = []
    word_list = []

    # First line gives us the analysed documents
    doc_list = index_file.readline()[:-1].split(',')[1:]

    for line in index_file.readlines():
        # Remove \n
        tmp = line[:-1].split(',')

        # Append first element to word_list
        word_list.append(tmp[0])

        # Append the rest of the array to index, transforming any string to integer
        # '1' -> 1
        index.append(list(map(int, tmp[1:])))

    # Lets parse search query

    # First lets get all the words replaced
    x_copy_no_logic = x.translate(str.maketrans('', '', string.punctuation.replace('\'', ''))).lower()
    for word in x_copy_no_logic.split():
        # For each word, replace in x with equivalent array
        if word not in word_list:
            return list(compress(doc_list, [0] * len(doc_list)))
        x = x.replace(word, 'np.array(' + str(list(map(bool, index[word_list.index(word)]))) + ')')


    # Now lets replace operations
    x = x.replace('&&', '&')
    x = x.replace('||', '|')
    x = x.replace('!', 'np.logical_not')

    return list(compress(doc_list, eval(x).tolist()))