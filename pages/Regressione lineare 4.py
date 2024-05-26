import pandas as pd
import numpy as np
from sklearn import linear_model
import streamlit as st
import math

# esempio tratto da https://www.startertutorials.com/blog/linear-regression-with-multiple-variables-in-python.html

st.title("Regressione lineare semplice con più variabili")
st.subheader('In questo esempio si mostra la previsione di un valore', divider='rainbow')


df = pd.read_csv("./dati/housepricesmv.csv")
median_bedrooms = math.floor(df.bedrooms.median())

df.bedrooms = df.bedrooms.fillna(median_bedrooms)

reg = linear_model.LinearRegression()
reg.fit(df[['area', 'bedrooms', 'age']], df.price)

st.write("Valore previsto")
st.write(reg.predict([[3000, 3, 40]]))

st.write("Valore previsto")
st.write(reg.predict([[2500, 4, 5]]))










