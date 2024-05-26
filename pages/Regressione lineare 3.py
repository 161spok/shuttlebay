import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import streamlit as st

# esempio tratto da https://www.startertutorials.com/blog/linear-regression-single-variable-in-python.html

st.title("Regressione lineare semplice con una variabile")
st.subheader('In questo esempio si mostra la previsione di un valore', divider='rainbow')

df = pd.read_csv('./dati/houseprices.csv')

plt.xlabel("Area(sq.ft.)")
plt.ylabel("Price($)")
plt.scatter(df.Area, df.Price)

reg = linear_model.LinearRegression()
reg.fit(df[['Area']], df.Price)
valore=reg.predict([[3300]])
st.write("Valore previsto",valore)

