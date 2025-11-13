import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop = set(stopwords.words('english'))

model = joblib.load('model.joblib')
vectorizer = joblib.load('vectorizer.joblib')

def clean_text(text):
    text = str(text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    words = [w for w in text.split() if w not in stop and len(w)>2]
    return " ".join(words)

st.title("📰 Fake News Detection")
st.write("Paste news article or headline below:")

input_text = st.text_area("Enter news here:")

if st.button("Predict"):
    cleaned = clean_text(input_text)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    if prediction == 1:
        st.error("🚨 This looks like **FAKE** news!")
    else:
        st.success("✅ This looks like **REAL** news!")