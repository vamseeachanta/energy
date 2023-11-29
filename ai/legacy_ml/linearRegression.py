import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt

from sklearn.datasets import load_boston
boston = load_boston()
#print(boston)

df_x = pd.DataFrame(boston.data,columns=boston.feature_names)
df_y = pd.DataFrame(boston.target)

#Get statistics description of the Data Frame
#print(df_x.describe())

reg = linear_model.LinearRegression()

x_train,x_test,y_train,y_test = train_test_split(df_x,df_y, test_size = 0.2, random_state = 5)

reg.fit(x_train,y_train)

print (reg.fit)
print (reg.coef_)

y_test_predict= reg.predict(x_test)

plt.plot(y_test,y_test)
plt.plot(y_test,y_test_predict, "o")
plt.xlabel('Measured Price', fontsize=14)
plt.ylabel('Predicted Price', fontsize=14)
plt.legend(['Perfect Fit', 'Linear Fit'], fontsize=14)
plt.savefig('linearRegressoin.png', box_inches='tight')
plt.close()
