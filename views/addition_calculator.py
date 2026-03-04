import streamlit as st
import math
from functions.addition import add, subtract
st.title("pH-Rechner")

st.write("Berechne deine pH-Werte.")

typ= st.selectbox("Wähle den Lösungstyp", ["Säure", "Base"])

konzentration = st.number_input(
    "Konzentration (mol/L)",
    min_value=0.0,
    format="%.6f")

with st.form("addition_form"):
    nummer_1 = st.number_input("erste Zahl")
    nummer_2 = st.number_input("zweite Zahl")
    resultate = add(nummer_1, nummer_2)

    submitted = st.form_submit_button("Berechnen")
  
    if submitted:
        st.write(resultate)