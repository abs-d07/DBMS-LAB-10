import pandas as pd
import streamlit as st
from database import view_all_data, view_only_train_numbers, get_train, edit_train_data

def update():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Train_number', 'Train_name', 'Train_type', 'Train_source', 'Train_destination', 'Train_availability'])
    with st.expander("Current trains"):
        st.dataframe(df)
    list_of_trains = [i[0] for i in view_only_train_numbers()]
    selected_train = st.selectbox("train to Edit", list_of_trains)
    selected_result = get_train(selected_train)
    if selected_result:
        Train_number = selected_result[0][0]
        Train_name = selected_result[0][1]
        Train_type = selected_result[0][2]
        Train_source = selected_result[0][3]
        Train_destination = selected_result[0][4]
        Train_availability = selected_result[0][5]

        Train_type_list=["Mail", "Fast", "Superfast"]
        Train_availability_list=["Yes", "No"]

        col1, col2 = st.columns(2)
        with col1:
            new_train_number = st.text_input("Train Number:",Train_number)
            new_train_name = st.text_input("Train Name:",Train_name)
            new_train_type = st.selectbox("Train Type", ["Mail", "Fast", "Superfast"] , index=Train_type_list.index(Train_type ))
        with col2:
            new_train_source = st.text_input("Source",Train_source)
            new_train_destination = st.text_input("Destination",Train_destination)
            new_train_availability = st.selectbox("Train Availability", ["Yes", "No"] , index=Train_availability_list.index(Train_availability ))
        if st.button("Update train"):
            edit_train_data(new_train_number, new_train_name, new_train_type, new_train_source, new_train_destination, new_train_availability , Train_number, Train_name, Train_type, Train_source, Train_destination , Train_availability)
            st.success("Successfully updated:: {} to ::{}".format(Train_number, new_train_number))
    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Train_number', 'Train_name', 'Train_type', 'Train_source', 'Train_destination' , 'Train_availability'])
    with st.expander("Updated data"):
        st.dataframe(df2)
