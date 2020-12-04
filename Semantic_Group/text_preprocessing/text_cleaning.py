# Imports
import numpy as np
import re
import string
import progressbar
import logging
logger = logging.getLogger(__name__)

# Import spacy
import spacy
import it_core_news_sm
nlp_it = it_core_news_sm.load()


############
# STOPWORDS
############

# Import list of stopwords from it_stop_words.py
from it_stop_words import get_italian_stop_words
my_it_stop_words = get_italian_stop_words()

# Import spacy italian stopwords
from spacy.lang.it.stop_words import STOP_WORDS as it_spacy_stopwords

# Import NLTK italian stopwords
import nltk
nltk.download('stopwords')
it_nltk_stopwords = nltk.corpus.stopwords.words('italian')

it_stopwords = set(it_spacy_stopwords) | set(it_nltk_stopwords) | my_it_stop_words

for stopword in it_stopwords:
    nlp_vocab = nlp_it.vocab[stopword]
    nlp_vocab.is_stop = True
    

##########################
# TEXT CLEANING FUNCTIONS
##########################

PATTERNS = {'urls': re.compile(r'https?://\S+|www\.\S+'),
            'users': re.compile(r'@[\w]*'),
            #'hashtags': re.compile(r'#[\w]*'),
            'digits': re.compile(r'(?<!\w)\d+|\d+(?!\w)'),
            'emojis': re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
}


def remove_patterns(text, patterns=PATTERNS.values()):
    for pattern in patterns:
        r = re.findall(pattern, text)
        for i in r:
            text = re.sub(re.escape(i), '', text)   
    return text


def remove_spaces(text):
    return ' '.join(text.split())
    
    
translator = str.maketrans(dict.fromkeys(string.punctuation))
def remove_punctuation(text):
    return text.translate(translator)


def lower_casing(text):
    return(text.lower())
    

PRE_NLP_pipeline  = [remove_patterns, remove_spaces]
POST_NLP_pipeline = [remove_punctuation, remove_spaces, lower_casing]


def clean_sentence(sentence, PRE_NLP_processing = PRE_NLP_pipeline, POST_NLP_processing = POST_NLP_pipeline, nlp = nlp_it):
    
    for process in PRE_NLP_processing:
        sentence = process(sentence)
    pre_nlp_sentence = sentence
    
    nlp_sentence = nlp(pre_nlp_sentence)
    #tokens = []
    lemmas = []
    for token in nlp_sentence:
        if not (token.is_stop or token.is_punct):
            #tokens.append(token.text)
            lemmas.append(token.lemma_)
            
    #tokens_sentence = ' '.join(tokens)
    lemmas_sentence = ' '.join(lemmas)
    
    for process in POST_NLP_processing:
        #tokens_sentence = process(tokens_sentence)
        lemmas_sentence = process(lemmas_sentence)
        
    return lemmas_sentence


def clean_content(data, PRE_NLP_processing = PRE_NLP_pipeline, POST_NLP_processing = POST_NLP_pipeline, nlp = nlp_it):

    logger.info('Cleaning content')
    cleaned_text = []
    for text in progressbar.progressbar(data):
        cleaned_text.append(
            clean_sentence(text, PRE_NLP_processing, POST_NLP_processing, nlp))
    return cleaned_text
