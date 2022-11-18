import pandas as pd
import streamlit as st
from database import view_all_data

def read():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Train_number', 'Train_name', 'Train_type', 'Train_source', 'Train_destination', 'Train_availability'])
    with st.expander("View all Trains"):
        st.dataframe(df)

