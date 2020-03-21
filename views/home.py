from views.base import BaseView
import streamlit as st

class HomepageView(BaseView):
    name = 'Homepage'
    
    def display(self):
         st.title('Homepage')
         return 