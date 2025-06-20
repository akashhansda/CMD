import streamlit as st
import joblib
import pandas as pd

# Load your trained model (must be uploaded or retrain here)
model = joblib.load("malware_model.pkl")

st.title("🔍 Cryptographic Malware Detector")

# Input
filename = st.text_input("Enter filename or feature string:")

# Fake conversion: simulate vectorization
def simple_feature(name):
    return pd.DataFrame([[len(name), name.count("x"), "mal" in name.lower()]], columns=["length", "x_count", "has_mal"])

# Predict
if st.button("Predict"):
    if filename.strip() == "":
        st.warning("Please enter a valid input.")
    else:
        features = simple_feature(filename)
        prediction = model.predict(features)[0]
        result = "🛑 Malware" if prediction == 1 else "✅ Benign"
        st.success(f"Prediction: {result}")
