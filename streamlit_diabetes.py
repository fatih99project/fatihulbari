import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

#judul web
st.title ('Data Mining Prediksi Diabetes')

Pregnancies = st.text_input('input nilain Pregnancies')

Glucose = st.text_input('input nilain Glucose')
BloodPressure = st.text_input('input nilain Blood Presure')
SkinThickness = st.text_input('input nilain Skin Thickness')
Insulin = st.text_input('input nilain Insulin')
BMI = st.text_input('input nilain BMI')
DiabetesPedigreeFunction = st.text_input('input nilain Diabetes Pedigree Function')
Age = st.text_input('input nilain Age')

#code untuk prediksi
diab_diagnosis =''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

    if(diab_prediction [0] == 1):
        diab_diagnosis = 'pasien terkena diabetes'
    else:
        diab_diagnosis = 'pasien tidak terkena diabetes'
    st.success(diab_diagnosis)