import streamlit as st
import math
from functions.addition import add, subtract
st.title("pH-Rechner")

st.write("Berechnet deine pH-Werte für dich.\n\nPflichtfelder sind mit einem Sternchen (*) gekennzeichnet und müssen für optimale Berechnungen ausgefüllt werden :)")

typ= st.selectbox("Wähle den Lösungstyp", ["Säure", "Base"])

konzentration = st.number_input(
    "Konzentration (mol/L)*",
    min_value=0.000001,
    format="%.6f")

if st.button("pH-Wert berechnen"):
    if typ == "Säure":
        pH = -math.log10(konzentration)
        st.write(f"Der pH-Wert der Säure beträgt: {pH:.2f}")
    else:
        pOH = -math.log10(konzentration)
        pH = 14 - pOH
        st.write(f"Der pH-Wert der Base beträgt: {pH:.2f}")

