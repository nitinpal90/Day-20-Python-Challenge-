#!/usr/bin/env python
# coding: utf-8

# # Day-20 Python Challenge

# ## Plotly Library

# In[2]:


x = [1,2,3,4,5,6,7,8,9,10]
y = [2,3,4,6,7,4,8,9,10,3]


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


plt.plot(x,y, color = 'b')
plt.title("Line Graph")
plt.show()


# In[5]:


import plotly.express as px


# In[10]:


fig = px.line(x=x, y=y, title = 'Line Graph')
fig.show()


# In[11]:


import plotly.graph_objects as go


# In[14]:


fig = go.Figure(go.Scatter(x=x, y=y))
fig.show()

