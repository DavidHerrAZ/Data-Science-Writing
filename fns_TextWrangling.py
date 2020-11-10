# text analysis, mining, and sentiment
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = stopwords.words("english")
lemmatizer = WordNetLemmatizer()


def tokenize(text):
    # normalize case and remove punctuation
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())

    # tokenize text
    tokens = word_tokenize(text)

    # lemmatize andremove stop words
    tokens = [lemmatizer.lemmatize(word)
              for word in tokens if word not in stop_words]

    return tokens


def tokenize_text_columns(dataframe_list, column_list):

    for dataframe in dataframe_list:
        for col in column_list:
            colname = col + '_tokenized'
            dataframe[colname] = dataframe[col].apply(str).apply(tokenize)
