import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

lemma = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


class cleantext():

    def __init__(self, text) -> None:
        self.text = text

    def Clean_text(self):
        cleaned_txt = re.sub(r'http\S+', '', self.text)
        cleaned_txt = re.sub('[^a-zA-Z]', ' ', self.text)
        cleaned_txt = str(cleaned_txt).lower()
        token_txt = word_tokenize(cleaned_txt)
        no_stop_txt = [item for item in token_txt if item not in stop_words]
        le = [lemma.lemmatize(word=w, pos='v') for w in no_stop_txt]
        lem = [i for i in le if len(i) > 2]

        return ' '.join(lem)
