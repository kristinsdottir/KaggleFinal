import luigi
import os

class TokenCounter(luigi.Task):
    def run(self):
        os.system('python pipeline/sentence_to_tokens.py')

    def output(self):
        return luigi.LocalTarget('data/tokens.json')

class TokenVector(luigi.Task):
    def requires(self):
        return TokenCounter()

    def run(self):
        os.system('python pipeline/tokens_to_vec.py')

    def output(self):
        return luigi.LocalTarget('data/tokens.csv')

if __name__ == '__main__':
    TokenVector().run()
