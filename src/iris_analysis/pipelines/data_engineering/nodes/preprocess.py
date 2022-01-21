# utilities
import pandas as pd
#import matplotlib.pyplot as plt
from emot.emo_unicode import EMOTICONS_EMO
import re

# nltk
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
#nltk.download()
#nltk.download('wordnet')
from .utils import abbr_dict, slang_dict
# Primary Functions


def clean_raw_data(data: pd.DataFrame) -> pd.DataFrame:
    '''
    Select pertinent columns from the full dataset.
    
     Args:
        data: Source data.
        
     Returns:
        Cleaned data.
        
    '''
    _pertinent_columns = ['sentiment', 'text']
    data = data[_pertinent_columns]
    
    return data
    
def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    '''
    Preprocess pertinent data.
    
     Args:
        data: Cleaned data.
        
     Returns:
        Processed data.
        
    '''
    data['text'] = data['text'].apply(_convert_links)
    data['text'] = data['text'].apply(_convert_usernames)
    #data['text'] = data['text'].apply(_convert_emoticons)
    data['text'] = data['text'].apply(_lemmatize)

    return data

def imputation(DataFrame):
    DataFrame = DataFrame.dropna(axis=0)
    return DataFrame

# Seconday Functions

def _convert_emoticons(text: str) -> str:
    for emot in EMOTICONS_EMO:
        text = re.sub(emot, EMOTICONS_EMO[emot], text)
    return text
    
def _convert_links(text: str) -> str:
    text = str(text)
    text = re.sub(r'(https?://\S+)|(www.\S+)', ' link ', text, flags = re.IGNORECASE)
    return text
    
def _convert_usernames(text: str) -> str:
    text = str(text)
    text = re.sub(r'@\S+', ' username ', text)
    return text
    
def _lemmatize(text: str) -> str:
    stop_words = stopwords.words('english')
    lemmatizer = WordNetLemmatizer()
    text = text.lower()
    text = [lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words]
    return ' '.join(text)
    

def normalize_tweets(data: pd.DataFrame) -> pd.DataFrame:
    """Normalize tweets.

    Args:
        tweets (pd.DataFrame): Tweets that have been cleanup regarding the
        use of characters and punctuations.


    Returns:
        pd.DataFrame: Tweets with cleaned up language.
    """
    # replace nan, abbreviations and slang
    primary_tweets = (
        data.dropna().replace(abbr_dict, regex=True).replace(slang_dict, regex=True)
    )

    return primary_tweets


