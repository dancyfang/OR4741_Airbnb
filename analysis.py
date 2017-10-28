import pandas as pd 
import numpy as np
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pdb

# read pd
df = pd.read_csv('MN_result.csv')
df = df[['AssessTot','LotArea','BldgArea','LotFront','BldgFront','ResidFAR','CommFAR','FacilFAR','NumBldgs','UnitsRes','UnitsTotal','YearBuilt','YearAlter']]
# pdb.set_trace()
# convert to np
data = df.as_matrix()

# scaling
data_scaled = preprocessing.scale(data)

# partitioning into X,y training,testing
X_train = data_scaled[0:10000,1:]
Y_train = data_scaled[0:10000,0]
X_test = data_scaled[10000:,1:]
Y_test = data_scaled[10000:,0]

# create linear regression object
regr = linear_model.LinearRegression()

# train the model
regr.fit(X_train,Y_train)

# test the model
Y_pred = regr.predict(X_test)

# the coefficients
print('attributes:\n',df.columns[1:])
print('coefficients:\n', regr.coef_)
# mean squared error
print('mean_squared_error:%.2f', mean_squared_error(Y_test,Y_pred))
# r2 score
print('r2_score:%.2f', r2_score(Y_test,Y_pred))