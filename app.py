import streamlit as st

from views.home import HomepageView
from views.nlp import NlpView

views_list = [
    HomepageView,
    NlpView
    ]
views_dict = {
    view.name: view()
     for view in views_list
     }

def main():
    page = st.sidebar.selectbox("Choose a page", list(views_dict.keys()))
    views_dict[page].display()
       

if __name__ == '__main__':
    main()