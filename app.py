import streamlit as st
import pandas as pd
import joblib

model = joblib.load("logistic_heart.pkl")
scaler = joblib.load("scaler.pkl")  
expected_columns = joblib.load("columns.pkl")

st.title("Heart Disease Prediction App")
st.markdown("provide the following details for prediction")

age = st.slider("Age", 18, 100,40)
sex = st.selectbox("Sex", ['M', 'F'])  # 'M' for male, 'F' for female
chest_pain = st.selectbox("Chest Pain Type", ['ATA', 'NAP', 'TA', 'ASY'])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dl)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
resting_ecg = st.selectbox("Resting ECG Results", ['Normal', 'ST-T Abnormality', 'Left Ventricular Hypertrophy'])
max_hr = st.number_input("Maximum Heart Rate Achieved", 60, 220, 150)
exercise_angina = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("Oldpeak (ST depression induced by exercise)", 0.0, 10.0, 1.0)
st_slope = st.selectbox("Slope of the peak exercise ST segment", ['Up', 'Flat', 'Down'])

if st.button("Predict"):
    raw_imput = {
        'age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol, 
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex' : sex,
        'ChestPainType' : chest_pain,
        'RestingECG' : resting_ecg,
        'ExerciseAngina' : exercise_angina,
        'ST_Slope' : st_slope
    }

    input_df = pd.DataFrame([raw_imput])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        st.error("The model predicts that the patient has heart disease.")
    else:
        st.success("Pheww you're in luck! The patient has low risk of heart disease.")

