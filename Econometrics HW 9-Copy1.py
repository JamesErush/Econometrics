#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd


# In[7]:


import numpy as np


# In[8]:


import matplotlib.pyplot as plt 


# In[19]:


from sklearn.linear_model import LinearRegression


# In[20]:


import scipy.stats as sci


# In[10]:


data = pd.read_excel(r'C:\Users\tim39\Downloads\caschool.xlsx')  # load data set
X = data.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
Y = data.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(X)  # make predictions


# In[11]:


plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.show()


# In[14]:


print(linear_regressor.intercept_)


# In[17]:


print(linear_regressor.coef_)


# In[18]:


data.var()


# In[ ]:


print(linear_regressor.)


# In[ ]:




