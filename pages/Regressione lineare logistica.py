'''
Tutorial Regressione Logistica
Created by - INTELLIGENZA ARTIFICIALE ITALIA
'''

#La regressione logistica è un algoritmo di apprendimento automatico supervisionato 
#utilizzato principalmente per attività di classificazione in cui l'obiettivo è prevedere 
#la probabilità che un'istanza appartenga o meno a una determinata classe. È una sorta di 
#algoritmo statistico, che analizza la relazione tra un insieme di variabili indipendenti 
#e le variabili binarie dipendenti. È uno strumento potente per il processo decisionale. 
#Ad esempio, e-mail di spam o meno. 

# importiamo le librerie
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# carichiamo il dataset
train_data = pd.read_csv('train-data.csv')
test_data = pd.read_csv('test-data.csv')


print(train_data.head())

# stampiamo le dimensioni del dataset
print('Dimensione dati allenamento :',train_data.shape)
print('Dimensione dati test :',test_data.shape)

# variable - target - Survived

# separiamo le variabili dipendenti dalle indipendenti
train_x = train_data.drop(columns=['Survived'],axis=1)
train_y = train_data['Survived']

# facciamo lo stesso sui dati di test
test_x = test_data.drop(columns=['Survived'],axis=1)
test_y = test_data['Survived']

'''
Creiamo il nostro modello !

Per saperne di più visita il link qui sotto
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

 '''
model = LogisticRegression()

# alleniamo il modello
model.fit(train_x,train_y)

# stampiamo i coefficienti
print('Coefficienti del modello :', model.coef_)

print('Intercept of model',model.intercept_)

# facciamo la nostra previsione
predict_train = model.predict(train_x)
print('Dati previsti allenamento :',predict_train) 

# Accuray Score 
accuracy_train = accuracy_score(train_y,predict_train)
print('Accuratezza del modello sui dati di allenamento : ', accuracy_train)

# pfacciamo la nostra previsione sui dati test
predict_test = model.predict(test_x)
print('Dati previsti test : ',predict_test) 

# Accuracy Score 
accuracy_test = accuracy_score(test_y,predict_test)
print('Accuratezza del modello sui dati di test : ', accuracy_test)