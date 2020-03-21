# Streamlit Dashboard 
A simple setup to deploy streamlit dashboard on Heroku. See it in action here: https://robin-streamlit.herokuapp.com/ 

To create a new page:
1. Create a new view in the `view/{view_name}.py` following this template
```python
from views.base import BaseView
import streamlit as st

class HomepageView(BaseView):
    name = 'Homepage'
    
    def display(self):
         st.title('Homepage')
         return 
```
whatever you will put in the display method will be displayed when your page is selected.

2. Import your view and add it to the `VIEWS_LIST` variable in `app.py`