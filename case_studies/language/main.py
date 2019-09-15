import os
import string
from collections import Counter
import pandas as pd
from matplotlib import pyplot as plt

text = 'The good, the bad, the ugly is a good movie.'

def count_words(text):
    text = text.lower()
    for p in string.punctuation:
        text = text.replace(p, '')
    
    return Counter(text.split(' '))

# print(len(count_words("This comprehension check is to check for comprehension.")))

def read_book(title_path):
    '''
    Reads a book and returns ist as a string
    '''
    with open(title_path, 'r', encoding='utf-8') as current_file:
        text = current_file.read()
        text = text.replace('\n', '').replace('\r', '')
    return text


def word_stats(word_counts):
    ''' Return number of unique words and frequencies '''
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)


book_dir = './books'

stats = pd.DataFrame(columns=['language', 'author', 'title', 'length', 'unique'])
title_num = 1
sep = os.path.sep
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + sep + language):
        for title in os.listdir(book_dir + sep + language + sep + author):
            inputfile = book_dir + sep + language + sep + author + sep + title
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language, author, title.replace('.txt',''), sum(counts), num_unique
            title_num+=1
            

english = stats[stats.language=='English']
german = stats[stats.language=='German']
plt.figure(figsize=(10,10))
plt.loglog(english.length, english.unique, 'o', label="English", color="crimson")
plt.loglog(german.length, german.unique, 'o', label="German", color="green")
plt.legend()
plt.xlabel("Book length")
plt.ylabel("Num unique words")
        
        