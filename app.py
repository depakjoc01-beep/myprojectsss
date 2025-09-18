import streamlit as st
import pickle
import numpy as np

# ---- Page Config ----
st.set_page_config(page_title="❤️ Heart Disease Predictor", page_icon="❤️", layout="centered")

# ---- Custom CSS ----
st.markdown("""
    <style>
    /* Background color */
    .stApp {
        background-color: #87CEFA; /* Light SkyBlue */
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: white;
        text-align: center;
    }
    .sub {
        font-size: 18px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    label, .stSelectbox label, .stNumberInput label {
        color: white !important;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #1d3557;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #457b9d;
        color: #f1faee;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Load Model ----
model = pickle.load(open("model.pkl", "rb"))

# ---- Title ----
st.markdown('<p class="title">❤️ Heart Disease Prediction</p>', unsafe_allow_html=True)
st.markdown('<p class="sub">By Divyanshu | Powered with Machine Learning</p>', unsafe_allow_html=True)

# ---- Layout with Columns ----
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 120)
    sex = st.selectbox("Sex", ["Female (0)", "Male (1)"])
    cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting BP", 50, 250)
    chol = st.number_input("Cholesterol", 100, 600)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    restecg = st.selectbox("Resting ECG (0–2)", [0, 1, 2])

with col2:
    thalach = st.number_input("Max Heart Rate", 60, 250)
    exang = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 10.0, step=0.1)
    slope = st.selectbox("Slope of Peak Exercise ST", [0, 1, 2])
    ca = st.selectbox("Major Vessels (0–3)", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia", [1, 2, 3])

# ---- Predict Button ----
if st.button("🔍 Predict"):
    input_data = np.array([[age, 1 if "Male" in sex else 0, cp, trestbps, chol,
                            fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    result = model.predict(input_data)

    if result[0] == 1:
        st.error("⚠️ High chance of Heart Disease detected.\n\nPlease consult a doctor immediately.")
    else:
        st.success("✅ You have a Low chance of Heart Disease.\n\nStay healthy and keep smiling! 😄")
