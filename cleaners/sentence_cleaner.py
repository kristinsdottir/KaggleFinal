import numpy as np
import enchant
import string
import re

from functools import reduce
from nltk.corpus import stopwords, words
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

class SentenceCleaner:
    def __init__(self):
        self.dictionary = enchant.Dict("en_US")
        self.stemmer = PorterStemmer()
        self.stopwords = set(stopwords.words("english"))
        self.punc_remover = str.maketrans('', '', string.punctuation)
        words_desc_order = sorted(set(words.words()), reverse=True)
        self.word_pattern = re.compile('|'.join(words_desc_order))

    def stem(self, word):
        stemmed = self.stemmer.stem(word)
        return stemmed if self.dictionary.check(stemmed) else word
    
    def split_nospace(self, word):
        return re.findall(self.word_pattern, word)

    def clean_sentence(self, sentence):
        # Get the review text, lowercase + remove punctuation
        review_text = sentence.lower().translate(self.punc_remover)
        words = word_tokenize(review_text)

        stems = []
        for word in words: 
            # Check if any words didn't have space
            for item in self.split_nospace(word): 
                # remove stopwords
                if item not in self.stopwords: 
                    # stem the word
                    stems.append(self.stem(item))

        return stems

    def get_bigrams(self, sentence):
        # Get the review text, lowercase + remove punctuation
        review_text = sentence.lower().translate(self.punc_remover)
        words = word_tokenize(review_text)

        words = reduce(lambda x, y: x+y, [self.split_nospace(word) for word in words])
        
        return zip(words[:-1], words[1:])