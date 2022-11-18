import pandas as pd
import streamlit as st
from database import view_all_data, view_only_train_numbers, delete_data

def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Train_number', 'Train_name', 'Train_type', 'Train_source', 'Train_destination', 'Train_availability'])
    with st.expander("Current data"):
        st.dataframe(df)
    list_of_trains = [i[0] for i in view_only_train_numbers()]
    selected_train = st.selectbox("Task to Delete", list_of_trains)
    st.warning("Do you want to delete: {}".format(selected_train))
    if st.button("Delete train"):
        delete_data(selected_train)
        st.success("train {} has been deleted successfully".format(selected_train))
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Train_number', 'Train_name', 'Train_type', 'Train_source', 'Train_destination', 'Train_availability'])
    with st.expander("Updated data"):
        st.dataframe(df2)
