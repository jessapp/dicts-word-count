# put your code here.

import string

import sys

def word_count(filename):

    my_file = open(filename)

    my_words = {}

    for line in my_file:
        # Strip off punctuation
        line = line.translate(None, string.punctuation)
        # Strip off trailing white space and split on spaces
        words = line.rstrip().split(" ")

        # Add word counts to dictionary
        for word in words:
            word = word.lower()
            my_words[word] = my_words.get(word, 0) + 1


    #for key_value in my_words.iteritems():
    #    print key_value[0], key_value[1]


    #for key in my_words:
    #   print key, my_words[key]

    for key, value in my_words.iteritems():
        print key, value

arg1 = sys.argv[1]

word_count(arg1)