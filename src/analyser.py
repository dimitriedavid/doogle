import os
import string
import numpy as np

word_list = []
index = []
doc_list = None


def analyseDocuments(folder):
    global doc_list
    global index
    global word_list

    # Get documents to analyse
    doc_list = os.listdir(os.getcwd() + '/' + folder + '/')
    doc_list.sort()

    # Go through each document
    for document in doc_list:
        file = open(folder + '/' + document, "r")

        for unformatted_line in file.readlines():
        
            # Replace all punctuation with spaces but keep ' like in can't
            line = unformatted_line.translate(str.maketrans('', '', string.punctuation.replace('\'', ''))).lower()

            words_in_line = line.split()
            for word in words_in_line:

                # Add word to word list
                if word not in word_list:
                    word_list.append(word)
                    index.append([0] * len(doc_list))

                # Mark word in index - corresponding document
                index[word_list.index(word)][doc_list.index(document)] = 1
    

def writeAnalysedIndexToFile(file):
    if doc_list is None:
        print('Documents not analysed. Please analyse first!')
        return

    output = open(file, "w")

    # No header on first column - just for nice viewing in excel
    output.write('word,')

    # First line prints indexed documents
    output.write(','.join(map(str, doc_list)))

    output.write('\n')

    # Print word, and doc aparitions
    for word in word_list:
        output.write(word + ',')
        output.write(','.join(map(str, index[word_list.index(word)])))
        output.write('\n')