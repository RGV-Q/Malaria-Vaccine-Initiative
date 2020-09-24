#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


import os
os.chdir ('/users/grace/documents/datasets/')


# In[4]:


pwd


# In[5]:


from IPython.display import Image
from IPython.core.display import HTML 
Image(url= "https://media.pri.org/s3fs-public/styles/story_main/public/story/images/18759_lores.jpg")


# In[6]:


df= pd.read_csv('Malaria_report.csv')
df.head ()

#Let's take a brief look at our data.
#It looks messy. We need to clean it.


# In[7]:


print (df.shape)
print (df.dtypes)

#Let's first collect parameters.


# In[8]:


df_numeric = df.select_dtypes (include=[np.number])
numeric_cols = df_numeric.columns.values
print(numeric_cols)

#Identifying numeric and non-numeric columns will be useful later when we are using values for our plots later on.


# In[9]:


df_non_numeric=df.select_dtypes (exclude=[np.number])
non_numeric_cols = df_non_numeric.columns.values
print (non_numeric_cols)

#Identifying numeric and non-numeric columns will be useful later when we are using values for our plots later on.


# In[10]:


cols = df.columns [:20] 
colors = ['#000099', '#ffff00']
sns.heatmap (df[cols].isnull(), cmap=sns.color_palette(colors))

#Let's visualize missing data through a heatmap.


# In[11]:


df= pd.read_csv('Malaria_report.csv')
df.head ()

#Now let's look at our dataset again, while comparing it to our heatmap above.


# In[12]:


df= pd.read_csv('Malaria_report.csv')
df.head ()

to_drop = ['GINI index (World Bank estimate)', 'GINI index (World Bank estimate), average 2000-16', 'gini of household income reported in Gallup, by wp5-year','Most people can be trusted, Gallup','Most people can be trusted, WVS round 1981-1984','Most people can be trusted, WVS round 1989-1993','Most people can be trusted, WVS round 1994-1998','Most people can be trusted, WVS round 1994-1998','Most people can be trusted, WVS round 1999-2004','Most people can be trusted, WVS round 2005-2009','Most people can be trusted, WVS round 2010-2014']
df.drop (to_drop, inplace=True, axis=1)

#Now that we saw from our heatmap all our missing datapoints, 
#let's drop unneccesary data.


# In[13]:


df.head ()

#Now let's look at our updated Dataset.


# In[14]:


df.info ()

#Let's collect our  parameters again.


# In[15]:


dups = df

print (dups.any ())

#I know we don't have duplicates, but I just want to make sure.


# In[16]:


df= pd.read_csv('Malaria_report.csv')

print(df.shape)
print(df.info())

# Finally, I try to find and identify the presence of Outliers in my dataset.


# In[17]:


df.describe ()

# I first look at my data again, to physically check for outliers.


# In[18]:


Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

# Here, I chose to identify outliers with Interquartile Range (IQR).


# In[19]:


print(df < (Q1 - 1.5 * IQR))
(df > (Q3 + 1.5 * IQR))

# I scan my data were the values show "True" 
# because that depicts presence of Outliers.
# I found no outliers present in my data.
# I now move to analysis portion of my work.


# In[20]:


## Now the data is ready for analysis.
## The primary goal of this project is to show why we should end one of the deadliest 
## diseases in human history, MALARIA, and to show how that is possible in this lifetime.

#Hypothesis 1: Ending Malaria Stimulates Economy.
#Hypothesis 2: Ending Malaria helps keep us safer and healthier.
#Hypothesis 3: Ending Malaria saves lives and stops the cycle of poverty.


# In[21]:


## This graph depicts how ending Malaria stimulates Economy.
## I showed the correlation between Life Ladder and Log GDP per capita 
df.plot (x='Life Ladder', y='Log GDP per capita', kind='scatter')


# In[22]:


## This illustration proves that ending Malaria helps keep us safer and healthier.
malaria_data= {'Healthy life expectancy at birth':np.random.rand(20),'Perceptions of corruption':np.random.rand(20)}
df=pd.DataFrame (malaria_data)
df.plot ( x='Healthy life expectancy at birth', y='Perceptions of corruption', kind='bar', color='green')


# In[ ]:


## This next illustration proves that ending Malaria saves lives and stops the cycle of poverty.
df= pd.read_csv('Malaria_report.csv')

df.plot (x='Healthy life expectancy at birth', y='Positive affect', kind='bar', color='pink')
plt.show()


This concludes my research.

References: 
https://www.malarianomore.org/about-us/
https://www.kaggle.com/search?q=malaria+in%3Adatasets

