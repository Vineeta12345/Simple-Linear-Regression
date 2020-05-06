# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:25:09 2020

@author: Vineeta
"""
import tkinter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
data=pd.read_csv("sales_data.csv",encoding='latin1')
data.shape
data.describe()
data.isnull().sum()
data = data.dropna(axis=1)
print(data)
sns.pairplot(data,x_vars=['QUANTITYORDERED','PRICEEACH','MSRP'], y_vars='SALES',height=4,
            aspect=1,kind='scatter')
plt.show()
import pandas as pd
from sklearn import linear_model
X = data[['QUANTITYORDERED','PRICEEACH','MSRP']]
Y = data['SALES']
regr = linear_model.LinearRegression()
regr.fit(X, Y)
QUANTITYORDERED = 56
PRICEEACH = 93.2
MSRP=150
print ('Predicted SalesPrice: \n', regr.predict([[QUANTITYORDERED,PRICEEACH,MSRP]]))
import tkinter as tk 
root = tkinter.Tk()
canvas1 = tk.Canvas(root, width = 500, height = 300)
canvas1.pack()
Intercept_result = ('Intercept: ', regr.intercept_)
label_Intercept = tk.Label(root, text=Intercept_result, justify = 'center')
canvas1.create_window(260, 220, window=label_Intercept)
Coefficients_result  = ('Coefficients: ', regr.coef_)
label_Coefficients = tk.Label(root, text=Coefficients_result, justify = 'center')
canvas1.create_window(260, 240, window=label_Coefficients)
label1 = tk.Label(root, text='Type QUANTITY ORDERED: ')
canvas1.create_window(100, 100, window=label1)
entry1 = tk.Entry (root)
canvas1.create_window(270, 100, window=entry1)
label2 = tk.Label(root, text=' Type PRICE EACH: ')
canvas1.create_window(120, 120, window=label2)

entry2 = tk.Entry (root) 
canvas1.create_window(270, 120, window=entry2)
label3 = tk.Label(root, text=' Type MSRP: ')
canvas1.create_window(140, 140, window=label3)

entry3 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 140, window=entry3)
def values(): 
    global New_QUANTITYORDERED #our 1st input variable
    New_QUANTITYORDERED = float(entry1.get()) 
    
    global New_PRICEEACH #our 2nd input variable
    New_PRICEEACH = float(entry2.get()) 
    
    global New_MSRP #our 2nd input variable
    New_MSRP = float(entry3.get()) 
    
    Prediction_result  = ('Predicted Sales Price: ', regr.predict([[New_QUANTITYORDERED ,New_PRICEEACH,New_MSRP]]))
    label_Prediction = tk.Label(root, text= Prediction_result, bg='orange')
    canvas1.create_window(260, 290, window=label_Prediction)
    
button1 = tk.Button (root, text='Predict Stock Index Price',command=values, bg='orange') # button to call the 'values' command above 
canvas1.create_window(270, 150, window=button1)
root.mainloop()

































