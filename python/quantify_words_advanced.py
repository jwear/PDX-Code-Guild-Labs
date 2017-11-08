from heapq import nlargest
from operator import itemgetter
import sys

# User input of text file name using command line
filename = sys.argv[1]

# Function that lists top 10 unique words in text file
def quantify_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data_file = file.read()
        for line in data_file:
            word_list = data_file.replace('?', '').replace('-','').replace('!', '').replace('"', '').replace(',', '').replace('.', '').lower().split()
            dic = {}
            for word in word_list:
                if word in dic:
                    dic[word] += 1
                else:
                    dic[word] = 1
            for key, value in nlargest(10, dic.items(), key=itemgetter(1)):
                print(key, value)
            break

# Call function
quantify_words(filename)
