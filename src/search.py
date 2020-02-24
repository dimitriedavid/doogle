import numpy as np
import string
from itertools import compress
import multiprocessing as mp

def findWord(word, index, word_list):
    return 'np.array(' + str(list(map(bool, index[word_list.index(word)]))) + ')'

def search(index_file, search_string):
    index_file = open(index_file, 'r')
    search_string = search_string.lower()
    doc_list = []
    index = []
    word_list = []
    pool = mp.Pool(mp.cpu_count())

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
    x_copy_no_logic = search_string.translate(str.maketrans('', '', string.punctuation.replace('\'', '')))
    if len(x_copy_no_logic.split()) == 0:
        pool.close()
        return list(compress(doc_list, [0] * len(doc_list)))
    for word in x_copy_no_logic.split():
        # For each word, replace in x with equivalent array
        if word not in word_list:
            pool.close()
            return list(compress(doc_list, [0] * len(doc_list)))
        search_string = search_string.replace(word, pool.apply(findWord, args=(word, index, word_list)))
    
    pool.close()

    # Now lets replace operations
    search_string = search_string.replace('&&', '&')
    search_string = search_string.replace('||', '|')
    search_string = search_string.replace('!', 'np.logical_not')

    return list(compress(doc_list, eval(search_string).tolist()))