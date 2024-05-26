import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# esempio tratto da https://www.askpython.com/python/examples/multiple-linear-regression

st.title("Regressione lineare multipla")
st.subheader('In questo esempio si utilizza Regressione lineare multipla', divider='rainbow')

dataset = pd.read_csv('./dati/50_Startups.csv')
dataset.head()
 
# data preprocessing
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4].values
 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_X = LabelEncoder() 
X[:,3] = labelEncoder_X.fit_transform(X[ : , 3])
  
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X), dtype=np.float64)
 
     
X = X[:, 1:]
 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
 
# Fitting the model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train) 
 
# predicting the test set results
y_pred = regressor.predict(X_test)

st.write("Valori di test")
st.write(y_test)
 
st.write("Valori previsti") 
st.write(y_pred)