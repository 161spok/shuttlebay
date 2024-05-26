import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("./dati/houseprices.csv")
model = linear_model.LinearRegression()
model.fit(df[['Area']], df.Price)
model.predict([[3300]])

import pickle

#We are opening a file named model_pickle in write binary mode
with open('model_pickle', 'wb') as f:
    #Dumping our model into the file referenced as f
    pickle.dump(model, f)

#We are opening a file named model_pickle in read binary mode
with open('model_pickle', 'rb') as f:
    #Loading our model into new_model
    new_model_pickle = pickle.load(f)

new_model_pickle.predict([[3300]])

import joblib

#Dumping the model into a file
joblib.dump(model, 'model_joblib')

new_model_joblib = joblib.load('model_joblib')

new_model_joblib.predict([[3300]])