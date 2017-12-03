from unittest import TestCase
from cleaners.sentence_cleaner import SentenceCleaner

global sc 
sc = SentenceCleaner()

class SentenceCleanerTest(TestCase):
    def test_split_nospace(self):
        self.assertEqual(sc.split_nospace('charityball'), ['charity', 'ball'])
        
    def test_clean_sentence(self):
        sentence = "walking on my way to SCHOOL!"
        tokens = sc.clean_sentence(sentence)
        self.assertEqual(tokens, ["walk", 'way','school'])

    def test_clean_sentence_with_nospace(self):
        sentence = "walking on my wayto SCHOOL!"
        tokens = sc.clean_sentence(sentence)
        self.assertEqual(tokens, ["walk", 'way','school'])