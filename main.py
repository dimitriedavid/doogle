import numpy as np

from analyser import analyseDocuments, writeAnalysedIndexToFile
from search import search

INDEX_NAME = 'index.csv'

def analyse(folder, output_name):
    analyseDocuments(folder)
    writeAnalysedIndexToFile(output_name)

x = input("Search query: ")

print(search(INDEX_NAME, x))
