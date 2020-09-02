import os
import nltk
import string


class Corpus(object):
    # rather than enter the data bit by bit, we create a constructor that takes in the data at one time 
    def __init__(self, corpus_dir):
        # all the attributes we want the class to have
        self.dir = corpus_dir # where corpus_dir is - the corpus' filepath
        # classes may contain functions we define ourselves, the all_files() function is defined below
        self.filenames = self.all_files()
        # this attribute calls nltk's built in English stopwords list and supplements it with punctuation and some extra characters we defined. 
        self.stopwords = nltk.corpus.stopwords.words('english') + [char for char in string.punctuation] + ['``', "''"]
        # for testing limiting to the first few texts - the [0:3] bit should be deleted to do all texts.
        self.texts = [Text(fn, self.stopwords) for fn in self.filenames]

    def all_files(self):
        """given a directory, return the filenames in it"""
        texts = []
        for (root, _, files) in os.walk(self.dir):
            for fn in files:
                if fn[0] == '.': # a new addition!
                    pass
                else:
                    path = os.path.join(root, fn)
                    texts.append(path)
        return texts
    
class Text(object):
    # now create the blueprint for our text object
    def __init__(self, fn, stopwords):
        # given a filename, store it
        self.filename = fn
        # a text has raw_text associated with it
        self.raw_text = self.get_text()
        # a text has raw tokens
        self.raw_tokens = nltk.word_tokenize(self.raw_text)
        # a text will have a clean version of those tokens
        self.cleaned_tokens = self.clean_tokens(stopwords)
        # we also want, in this case, to make an NLTK text object
        self.nltk_text = nltk.Text(self.cleaned_tokens)
        
    def get_text(self):
        with open(self.filename) as fin:
            return fin.read()
    
    def clean_tokens(self, stopwords):
        return [token.lower() for token in self.raw_tokens if token not in stopwords]
        
# this is what runs if you run the file as a one-off event - $ python3 class_practice.py
def main():
    corpus_dir = 'corpus/sonnets/'
    print('As mentioned above, this output presents as though it is being run from the command line.') # anything that you might want to jump to, such as a graph, FreqDist, etc. would go here

# this allows you to import the classes as a module. it uses the special built-in variable __name__ set to the value "__main__" if the module is being run as the main program.] 
if __name__ == "__main__":
    main()