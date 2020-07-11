from views.base import BaseView
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

DEFAULT_TEXT = """This sucked. Couple good songs but overall nothing more than a good community theater performance. The rapping was terrible and sounded like people trying to rap who have no idea how to rap. Miranda is particularly horrible at rapping and singing. Killed his character by putting himself in the lead when he's so far below the talent of the rest of the performers. Stick to writing, dude.
"""


class NlpView(BaseView):
    name = 'Natural language processing'
    analyzer = SentimentIntensityAnalyzer()

    def display(self):
         st.title('Natural language processing')
         text = st.text_area("label goes here", DEFAULT_TEXT)
         vs = self.analyzer.polarity_scores(text)
         st.write('## Vader sentiment')
         st.write(vs)
         st.write('## TextBlob')
         blob = TextBlob(text)

         for sentence in blob.sentences:
            st.write(sentence)
            st.write(sentence.sentiment)

