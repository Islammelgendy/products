from fastapi import FastAPI
import pickle

from CleanText import cleantext

app = FastAPI()


filename = './models/SVM_CLS.pkl'
cls = pickle.load(open(filename, 'rb'))
vectorizer = pickle.load(open("./models/vectorizer.pickle", 'rb'))


@ app.get("/")
async def root():
    return {"yaoota": "islam legendy"}


@ app.get("/get_category")
async def category(title: str = ''):
    title = cleantext(title).Clean_text()

    return {'category':
            str(cls.predict(vectorizer.transform([title]))[0])}
