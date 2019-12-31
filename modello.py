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


def fit_model():
    df_modello=fun.make_df_training()
    df_modello.sort_values(by="abitanti",inplace=True)

    plt.scatter(df_modello["abitanti"],df_modello["tot_entrate"])

    data_x = df_modello["abitanti"]
    data_y = df_modello["tot_entrate"]




    seed(1)


    rand_seed=randint(0, 100)

    randint(0,100)
    train_x, valid_x, train_y, valid_y = train_test_split(data_x, data_y, test_size=0.33, random_state = rand_seed)




    #log fitting
    def log_fit(x,A):
        return A*np.log(x+1)
    A=optimization.curve_fit(log_fit, train_x, train_y)[0][0]
    log=lambda x: A*np.log(x+1)



    # LinearRegression
    def lin_fit(x,m):
        return m*x
    m=optimization.curve_fit(lin_fit, train_x, train_y)[0][0]
    lin=lambda x: m*x


    #square root
    def sq_fit(x,k,n):
        return (k*x)**n
    k,n=optimization.curve_fit(sq_fit,train_x,train_y)[0]
    sq=lambda x: (k*x)**n

    # Comparison spline
    sequence=tuple(np.linspace(3000,1100000,20))
    transformed_x = dmatrix("bs(train, knots=sequence, degree=3, include_intercept=False)", {"train": train_x},return_type='dataframe')

    fit1 = sm.GLM(train_y, transformed_x).fit()

    pred1 = fit1.predict(dmatrix("bs(valid,knots= sequence, include_intercept=False)", {"valid": data_x}, return_type='dataframe'))





    plt.scatter(data_x, data_y, facecolor='k', edgecolor='k', marker="p",alpha=0.2)
    plt.plot(data_x,pred1,linewidth=3,label="spline")
    plt.plot(data_x,log(data_x),linewidth=3,label="log")
    plt.plot(data_x,lin(data_x),linewidth=3,label="linear")
    plt.plot(data_x,sq(data_x),linewidth=3,label="square")
    plt.legend()
    plt.show()





    #zoom in
    data_x_reduced=data_x[data_x<1200000]
    data_y_reduced=data_y[:len(data_x_reduced)]
    pred_reduced=fit1.predict(dmatrix("bs(valid,knots= sequence, include_intercept=False)", {"valid": data_x_reduced}, return_type='dataframe'))
    plt.scatter(data_x_reduced, data_y_reduced, facecolor='k', marker="p",edgecolor='k', alpha=0.2)
    plt.plot(data_x_reduced,pred_reduced,linewidth=3,label="spline")
    plt.plot(data_x_reduced,log(data_x_reduced),linewidth=3,label="log")
    plt.plot(data_x_reduced,lin(data_x_reduced),linewidth=3,label="linear")
    plt.plot(data_x_reduced,sq(data_x_reduced),linewidth=3,label="square")
    plt.legend()
    plt.show()





    rms_log = np.sqrt(mean_squared_error(valid_y, log(valid_x)))
    rms_square=np.sqrt(mean_squared_error(valid_y, sq(valid_x)))
    rms_lin=np.sqrt(mean_squared_error(valid_y, lin(valid_x)))
    print("{:>35}".format("RMS"),"\nlin m= %.5f"%m,'{:>35}'.format(rms_lin),"\nlog A= %.5f"%A,"{:>33}".format(rms_log),"\nsquare k=%.4f  n=%.4f"%(k,n),"{:>20}".format(rms_square))

    return k,n
