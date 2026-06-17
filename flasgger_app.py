from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import os
import flasgger
from flasgger import Swagger

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CLASSIFIER_PATH = os.path.join(BASE_DIR, "classifier.pkl")

app = Flask(__name__)
Swagger(app)

pickle_in = open(CLASSIFIER_PATH, "rb")
classifier = pickle.load(pickle_in)

@app.route('/',methods=['GET'])
def welcome():
    """
    Welcome Endpoint
    ---
    responses:
      200:
        description: Returns a welcome message.
    """
    return "Welcome All"

@app.route('/predict')
def predict_note_authentication():
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
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted value is: "+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """
    Predict Multiple Notes from CSV
    ---
    consumes:
      - multipart/form-data
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        description: CSV file containing variance, skewness, curtosis, and entropy columns.
    responses:
      200:
        description: List of predictions for all records in the uploaded CSV file.
    """
    df_test=pd.read_csv(request.files.get("file"))
    prediction=classifier.predict(df_test).tolist()
    prediction = [int(x) for x in prediction]
    return "The predicted values for the csv is: "+str(list(prediction))

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)