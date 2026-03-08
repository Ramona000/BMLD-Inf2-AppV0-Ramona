import streamlit as st
import math
from functions.addition import add, subtract
st.title("pH-Rechner")

st.write("Berechnet deine pH-Werte für dich.\n\nPflichtfelder sind mit einem Sternchen (*) gekennzeichnet und müssen für optimale Berechnungen ausgefüllt werden :)")

pH = None 

with st.form("pH_form"):
    typ= st.selectbox("Wähle deinen Lösungstyp", ["starke Säure", "starke Base"])

    konzentration = st.number_input(
    "Konzentration (mol/L)*",
    min_value=0.000001,
    format="%.6f")

    submitted = st.form_submit_button("pH-Wert berechnen")

if submitted:
    if typ == "starke Säure":
        pH = -math.log10(konzentration)
        st.success(f"Der pH-Wert der Säure beträgt: {pH:.2f}")
    else:
        pOH = -math.log10(konzentration)
        pH = 14 - pOH
        st.success(f"Der pH-Wert der Base beträgt: {pH:.2f}")


    if pH < 7:
        st.info("Die Lösung ist sauer.")
    elif pH == 7:
        st.info("Die Lösung ist neutral.")
    else:
        st.info("Die Lösung ist basisch.")

