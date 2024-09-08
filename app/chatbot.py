import streamlit as st
import pickle
import nltk
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.pipeline import Pipeline
import re

nltk.download('punkt_tab')

# Define the preprocess_and_tokenize function used during training
def preprocess_and_tokenize(data):
    # remove html markup
    data = re.sub("(<.*?>)", "", data)

    # remove urls
    data = re.sub(r'http\S+', '', data)

    # remove hashtags and @names
    data = re.sub(r"(#[\d\w\.]+)", '', data)
    data = re.sub(r"(@[\d\w\.]+)", '', data)

    # remove punctuation and non-ascii digits
    data = re.sub("(\\W|\\d)", " ", data)

    # remove whitespace
    data = data.strip()

    # tokenization with nltk
    data = word_tokenize(data)

    # stemming with nltk
    porter = PorterStemmer()
    stem_data = [porter.stem(word) for word in data]

    return stem_data

filename = 'models/tfidf_svm.sav'
model = pickle.load(open(filename, 'rb'))

class_names = ['Joy', 'Sad', 'Anger', 'Neutral', 'Fear', 'Love']

def get_response(prediction):
    responses = {
        'Joy': "Teks yang Anda masukkan masuk dalam kategori 'Joy' atau 'Menyenangkan'",
        'Sad': "Teks yang Anda masukkan masuk dalam kategori 'Sad' atau 'Sedih'",
        'Anger': "Teks yang Anda masukkan masuk dalam kategori 'Anger' atau 'Marah'",
        'Neutral': "Teks yang Anda masukkan masuk dalam kategori 'Neutral' atau 'Netral'",
        'Fear': "Teks yang Anda masukkan masuk dalam kategori 'Fear' atau 'Takut'",
        'Love': "Teks yang Anda masukkan masuk dalam kategori 'Love' atau 'Cinta'",
    }
    return responses.get(prediction, "Emosi tidak dikenali")

st.title('Text Emotion Classification ChatBot')

message = st.text_input("Masukkan pesan Anda:")

if message:
    prediction = model.predict([message])[0]
    response = get_response(prediction)
    
    st.write(response)
