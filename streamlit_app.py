
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CLASSIFIER_PATH = os.path.join(BASE_DIR, "classifier.pkl")

pickle_in = open(CLASSIFIER_PATH, "rb")
classifier = pickle.load(pickle_in)

def welcome():
    """
    Welcome Endpoint
    ---
    responses:
      200:
        description: Returns a welcome message.
    """
    return "Welcome All"

def predict_note_authentication(variance,skewness,curtosis,entropy):
    """
    Predict Bank Note Authentication
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
        description: Variance of the image transformed data
      - name: skewness
        in: query
        type: number
        required: true
        description: Skewness of the image transformed data
      - name: curtosis
        in: query
        type: number
        required: true
        description: Curtosis of the image transformed data
      - name: entropy
        in: query
        type: number
        required: true
        description: Entropy of the image transformed data
    responses:
      200:
        description: Prediction result (0 = Fake Note, 1 = Authentic Note)
    """
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return " "+str(prediction)

def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("skewness","Type Here")
    curtosis = st.text_input("curtosis","Type Here")
    entropy = st.text_input("entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))

    if st.button("Predict from data file"):
        csv_path = os.path.join(DATA_DIR, "BankNote_Authentication.csv")
        df = pd.read_csv(csv_path)
        prediction = classifier.predict(df).tolist()
        prediction = [int(x) for x in prediction]
        st.success('Predictions from data file: {}'.format(prediction))

    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

if __name__=="__main__":
    main()