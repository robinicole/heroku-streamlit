from views.base import BaseView
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

class NlpView(BaseView):
    name = 'Natural language processing'
    analyzer = SentimentIntensityAnalyzer()

    def display(self):
         st.title('Natural language processing')
         text = st.text_input("label goes here", 'default')
         vs = self.analyzer.polarity_scores(text)
         st.write('## Vader sentiment')
         st.write(vs)
         st.write('## TextBlob')
         blob = TextBlob(text)

         for sentence in blob.sentences:
            st.write(sentence.sentiment)

