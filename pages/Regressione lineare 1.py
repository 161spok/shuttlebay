'''
Tutorial Regressione Lineare
Created by - INTELLIGENZA ARTIFICIALE ITALIA
'''

# importiamo le librerie
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import metrics


import streamlit as st

# Tratto da:
# https://365datascience.com/tutorials/python-tutorials/linear-regression/

st.title("Algoritmi ML 🎈")

st.subheader('Regressione lineare semplice', divider='rainbow')

# carichiamo il dataset
data = pd.read_csv('./dati/Simple_linear_regression.csv')

data.describe()

y = data['GPA'] # variabile dipendente
 
x1 = data['SAT'] # variabile indipendente
st.write("GPA variabile dipendente")

st.write("SAT variabile indipendente")

plt.scatter(x1,y)

plt.xlabel('SAT', fontsize = 20)

plt.ylabel('GPA', fontsize = 20)
  
#plt.show()
st.pyplot(plt.gcf()) 

x = sm.add_constant(x1)

results = sm.OLS(y,x).fit()
 
st.write(results.summary())

plt.scatter(x1,y)
 
yhat = 0.0017*x1 + 0.275
 
fig = plt.plot(x1,yhat, lw=4, c='orange', label = 'regression line')
 
plt.xlabel('SAT', fontsize = 20)
 
plt.ylabel('GPA', fontsize = 20)
 
#plt.show()
st.pyplot(plt.gcf())
#=====================================================================================================================




































