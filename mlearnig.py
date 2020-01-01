import funzioni as fun
import coorti as coo
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlt
import scipy.optimize as optimization
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt
from random import seed
from random import randint


from patsy import dmatrix
import statsmodels.api as sm
import statsmodels.formula.api as smf


coo.make_all_df()
df_modello=fun.make_df_training()
df_modello.columns
df_modello=df_modello.drop(df_modello.index[df_modello["volontari"]==0])
df_modello=df_modello.drop(df_modello.index[df_modello["luoghi_aperti"]==0])

df_test=df_modello[df_modello["abitanti"]<1200000]
plt.scatter(df_test["abitanti"],df_test["volontari"])



from sklearn import linear_model
# with sklearn
regr = linear_model.LinearRegression()
X=df_modello["abitanti"]
Y=df_modello[""]
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

# prediction with sklearn
New_Interest_Rate = 2.75
New_Unemployment_Rate = 5.3
print ('Predicted Stock Index Price: \n', regr.predict([[New_Interest_Rate ,New_Unemployment_Rate]]))

# with statsmodels
X = sm.add_constant(X) # adding a constant

model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)
