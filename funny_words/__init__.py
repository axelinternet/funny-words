#
# funny-words
# copyright 2016 Seth Black
# 11/09/2016
#

import argparse
import random
from word_list import marshmallow_words, alpha_words, writers_words
funny_words = marshmallow_words + alpha_words + writers_words
funny_words = [word.lower() for word in funny_words]


def pick_funny_word(but_not=u''):
    funny_word = random.choice(funny_words).lower()

    while funny_word == but_not:
        funny_word = random.choice(funny_words)

    return funny_word


def build_n_gram(words=2, join_with=u' ', all_start_with=None, first_letter=None):
    previous_words = u''
    local_funny_words = []

    if all_start_with != None:
        selected_words = random.sample(funny_words, words)
        for i in xrange(words):
            while selected_words[i][0] != all_start_with:
                selected_words[i] = random.choice(funny_words)
        return join_with.join(selected_words)

    if first_letter != None:
        selected_words = random.sample(funny_words, words)
        while selected_words[0][0] != first_letter:
            selected_words[0] = random.choice(funny_words)
        return join_with.join(selected_words)
    else:
        return join_with.join(random.sample(funny_words, words))

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            u'-w',
            u'--words',
            help=u'how many funny words to generate per line',
            type=int,
            default=2)
    parser.add_argument(
            u'-n',
            u'--number',
            help=u'how many lines of funny words to generate',
            type=int,
            default=1)
    parser.add_argument(
            u'-d',
            u'--delimiter',
            help=u'what to put between the funny words',
            type=str,
            default=u' ')
    parser.add_argument(
            u'-a',
            u'--allstart',
            help=u'Force all word to start with a specific letter',
            type=str,
            default=None)
    parser.add_argument(
            u'-s',
            u'--start',
            help=u'Force the first word to start with a specific letter',
            type=str,
            default=None)
    args = parser.parse_args()

    for n in xrange(args.number):
        print build_n_gram(args.words, args.delimiter, args.allstart, args.start)
