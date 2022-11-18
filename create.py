import streamlit as st
from database import add_data

def create():
    cola, colb = st.columns(2)
    with cola:
        Train_number = st.text_input("Train Number")
        Train_name = st.text_input("Train Name")
        Train_type = st.selectbox("Train Type",["Mail","Fast","Superfast"])
    with colb:
        Train_source = st.text_input("Source")
        Train_destination = st.text_input("Destination")
        Train_availability = st.selectbox("Availability",["Yes","No"])
    if st.button("Add Train"):
        add_data(Train_number, Train_name, Train_type, Train_source, Train_destination,Train_availability)
        st.success("Successfully added Train: {}".format(Train_number))
