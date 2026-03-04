import streamlit as st
from functions.addition import add, subtract
st.title("Addition")

st.write("Hier ist mein Rechner.")

with st.form("addition_form"):
    nummer_1 = st.number_input("erste Zahl")
    nummer_2 = st.number_input("zweite Zahl")
    resultate = add(nummer_1, nummer_2)

    submitted = st.form_submit_button("Berechnen")
  
    if submitted:
        st.write(resultate)