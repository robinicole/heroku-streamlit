import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from views.home import HomepageView

views_list = [HomepageView]
views_dict = {
    view.name: view()
     for view in views_list
     }

def main():
    page = st.sidebar.selectbox("Choose a page", list(views_dict.keys()))
    views_dict[page].display()
       

if __name__ == '__main__':
    main()