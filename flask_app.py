from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CLASSIFIER_PATH = os.path.join(BASE_DIR, "classifier.pkl")

app = Flask(__name__)
pickle_in = open(CLASSIFIER_PATH, "rb")
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict')
def predict_note_authentication():
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted value is: "+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    df_test = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test).tolist()
    prediction = [int(x) for x in prediction]
    return "The predicted values for the csv is: "+str(list(prediction))

@app.route('/predict_from_file')
def predict_note_file_from_data():
    csv_path = os.path.join(DATA_DIR, "BankNote_Authentication.csv")
    df_test = pd.read_csv(csv_path)
    prediction = classifier.predict(df_test).tolist()
    prediction = [int(x) for x in prediction]
    return "The predicted values for the csv is: "+str(list(prediction))

if __name__=="__main__":
    app.run()