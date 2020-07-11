"""
The Homepage
"""
import streamlit as st

from views.base import BaseView


class HomepageView(BaseView):
    """
    The Homepage
    """
    name = 'Homepage'

    def display(self):
        st.write('# Homepage')
