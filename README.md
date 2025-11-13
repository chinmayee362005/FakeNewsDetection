# FakeNewsDetection
"Fake News detection using AI and Streamlit"
Live Demo:**[Click here to open the app](https://fakenewsdetection-gsnae3x2kchddpeyepaxqd.streamlit.app/)

project overview:
A Machine Learning and Natural Language Processing (NLP) based project that classifies news articles as **Real** or **Fake**.  
It uses TF-IDF for text vectorization and Logistic Regression for classification.  
Deployed using **Streamlit Cloud** for live access.

Technologies used:
-python
-Pandas , Numpy
-NLTK
-Streamlit
-Joblib+

Model Performance
✅ **Accuracy:** 98.6%  
✅ **Precision, Recall, and F1-score** all above 0.97  
✅ Model trained on the Kaggle *Fake and Real News Dataset*

🧠 Steps Followed  
1. Data Cleaning (removing punctuation, URLs, stopwords)  
2. TF-IDF Vectorization  
3. Model Training (Logistic Regression)  
4. Model Saving (`model.joblib` & `vectorizer.joblib`)  
5. Web App Creation (`app.py`)  
6. Deployment on Streamlit Cloud  

💡 Future Improvements  
- Try advanced models (e.g., BERT or LSTM)  
- Add headline summarization  
- Enhance UI/UX with better visuals

👩‍💻 Author  
ChinmayeeS
BCA Final Year Student   
📧 Email: chinmayee362005@gmail.com  
🌐 GitHub:https://github.com/chinmayee362005

example for true news:
1) FBI Russia probe helped by Australian diplomat tip-off”, WASHINGTON (Reuters) - Trump campaign adviser George Papadopoulos’ comments to an Australian diplomat helped trigger the FBI investigation into Russian election interference.
2) U.S. military to accept transgender recruits on Monday: Pentagon”, WASHINGTON (Reuters) - Transgender people will be allowed for the first time to enlist in the    U.S. military starting Monday, after the Trump administration decided not to appeal a court ruling blocking its ban.

example for fake news:
1) Donald Trump Sends Out Embarrassing New Year’s Eve Message; This is Disturbing”, “Donald Trump just couldn’t wish all Americans a Happy New Year without controversy, sending out a message that sparked backlash online and in the media”.
2) “Drunk Bragging Trump Staffer Started Russian Collusion Investigation”, “House Intelligence Committee Chairman Devin Nunes is now looking into the allegation that a Trump staffer’s drunken boasting led to the launch of the Russia probe against the campaign”.
