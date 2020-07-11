"""
Main script to display all streamlit views
"""
import streamlit as st

from views.home import HomepageView
from views.nlp import NlpView

views_list = [
    HomepageView,
    NlpView
    ]
views_dict = {
    view.get_name(): view()
    for view in views_list
}

def main():
    """
    main method
    """
    page = st.sidebar.selectbox(
        "Choose a page",
        options=list(views_dict.keys())
    )
    views_dict[page].display()
       

if __name__ == '__main__':
    main()
