#!/usr/bin/env python
# coding: utf-8

# # Expenditure Data Analysis Project

# Index Table:
#     
# 1. Problem Statements:
# 2. Data Description:
#     
#    * 2.1 Introduction
#    * 2.2 Data source and data set
# 3. Load the packages and Data
# 4. Data Profiling:
#    * 4.1 Understanding the Dataset
#    * 4.2 Pre Profiling
#    * 4.3 Preprocessing
#    * 4.4 Post Profiling
# 5. Data Visualization:
# 6. Conclusions:    

# ## 1. Problem Statements:
# 
# No business can survive in this competitive market without managing their cost. It does not matter if revenues are high 
# but if cost is higher it is a red flag. So you are tasked to 
# help management in creating and establishing new structure 
# and models to reduce cost.

# ## 2. Data Description :
# 
# * Exp Category: Gives the description about expenditure Category .
# * State: Gives the description about States and Uts of India.
# * Year: Gives the description about Year.
# * Values : Gives the description about expenditure spending in millions.
# 
# The Dataset as listed on NITI Aayog Website from 1980_81 to 
# 2015_16. That is collected by using web scraping.
# 
# 
# ##2.1. Introduction:
# 
# An Expenditure Data Analysis the project releted to Exploratory data analysis(EDA) and Data Visualization of 
# expenditure information,visualize different aspects of it,
# and finally i worked at a few ways of analyzing the spending of expenditure based on its previous performance history statewise in India. The NITI Aayog(National Institution for Transforming India) serves as the apex public policy think tank of the Goverment of India, and the nodal agency tasked with catalyzing economic development, and fostering cooperative federalism through the involvement of State Goverments of India in the economic policy-making process 
# using a bottom-up apporach
# 
# ## 2.2 Data source and data Set:
# 
# The dataset as listed on NITI Aayog website from 1980_81 to 2015_16. That is collected by using web scraping.
# 
# You can find the dataset on the given link. https://www.niti.gov.in/
# 
# ## Approach 
# 
# The main goal of the project is to find key metrics and factors and show the meaningful relationships between attributes based on different features available in the dataset.
# 
# * Do ETL : Extract-Transform-Load the dataset and find for some information from this large data. This is from of data mining.

# ## 3. Load the Package and Data

# 1. Import Libraries

# In[3]:


import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()


# 2. Loading data

# In[8]:


expenditure = pd.read_excel("Downloads/final_expenditure.xlsx")


# In[9]:


expenditure.head()


# ## 4.Data Profiling:
# 
# ## 4.1. Understanding the Dataset

# In[10]:


expenditure.shape # To know shape of dataset


# * Their are 8753 rows and 4 columns in dataset after combining.

# In[11]:


expenditure.size  # to show the total no. of volume(elements) 


# In[12]:


expenditure.columns # to show each columns name in dataset


# In[13]:


expenditure.dtypes  # to shows data types of each column name


# In[14]:


expenditure.describe() # To show Statistic information of dataset


# In[15]:


expenditure.describe(include = 'all') # To show Statistics information of all dataset


# In[16]:


expenditure.info()  # to show indexes , data types each columns name


# In[17]:


#Finfing how many unique values are in the dataset
expenditure.nunique()


# In[18]:


expenditure['Year'].unique() # unique values in year columns


# * This Dataset contains from year 1980-81 to 2015-16.

# In[19]:


expenditure['Exp Category'].unique() # categories of expenditure


# In[20]:


expenditure['State'].unique() # unique Values in State columns


# * These are the names of States and UTs of India.

# ## 4.2 Preprofiling:
# 
# By pandas profiling, an interctive HTML report gets generated 
# which contains all the information about the columns of the dataset, like the 
# counts and type of each column.
# 
# 1. Detailed information about each column, coorelation between different
#    columns and a sample of dataset
#     
# 2. It gives us visual interpretation of each column in the data.
# 3. Spread of the data can be better understood by the distribution plot.
# 4. Grannular level analysis of each column.

# Now performing pandas profiling to understand data better.

# In[21]:


import pandas_profiling as prf


# To generate the standard profiling report,merely run:

# In[22]:


expenditure_profile = prf.ProfileReport(expenditure)
expenditure_profile


# In[23]:


# save profile
expenditure_profile.to_file(output_file="expenditure_before_preprocessing.html")


# ## 4.3 preprocessing
# 
# Modified the structure of data in order to make it more understandable and 
# suitable and convenient for statistical analysis.
# 
# 1. Checking null Values 
# 2. Filling null values
# 3. Checking and removing Duplicates rows

# 1. Checking null Values

# In[24]:


m = expenditure.isnull().sum()


# In[25]:


m


# In[26]:


#missing Values in percentage
m1 = m/len(expenditure)*100


# In[27]:


m1


# In[28]:


#missing values with %
pd.concat([m,m1],axis = 1,keys =['Total','Missing %'])


# * Year having 0.19% and value having 2.4% missing values contains in the dataset
# 

# # Null values shown by heatmap

# In[29]:


sns.heatmap(expenditure.isnull())


# 2. Filling Null values
# 
#  * filling null values with 0.

# In[30]:


# make copy of dataset before changes
exp_data = expenditure.copy()
exp_data.head()


# In[31]:


exp_data.fillna(0,inplace = True)


# In[32]:


#checking missing values again
exp_data.isnull().sum()


# # 3. Checking and removing Duplicates rows

# In[33]:


exp_data[exp_data.duplicated()]  # duplicates rows


# In[34]:


expenditure.duplicated().sum() #number of duplicates rows


# * only 4 rows are duplicates.
# * so lets drop them for better analysis.

# In[35]:


exp_data.drop_duplicates(inplace=True)


# In[36]:


#again checking for duplicates
exp_data.duplicated().sum()


# In[37]:


#checking size after cleaning
exp_data.shape


# # 4.4 Post Profiling 
# 
# * Post profiling after cleaning dataset.

# In[38]:


exp_clean_profile = prf.ProfileReport(exp_data)
exp_clean_profile


# In[39]:


# save clean profile file

exp_clean_profile.to_file(output_file="expenditure_after_preprocessing.html")


# In[40]:


#save clean dataset into csv
exp_data.to_csv('expenditure1.csv')


# 5. Data Visualization:
# Data visualization is concerned with visually presenting sets of primarily quantitative raw data in a schematic form. The visual formats used in data visualization include tables, charts and graphs.
# 
# In this project we use matplotlib and seaborn python libraries.

# 1. Correlation between features

# In[41]:


corr = exp_data.corr()
corr


# * There is no feature for correlation.

# 2. All unique categories of expenditure.

# In[42]:


exp_data.head(2)


# In[43]:


exp_data['Exp Category'].nunique()


# In[44]:


sns.countplot(exp_data['Exp Category'],orient='v')
#sns.set_theme(style = "darkgrid")
plt.xticks(rotation=90)


# Insights : If we ignore Exp Category, Its clearly shown there are 8 expenditure
#     categories in this NITI Aayog dataset.

# # 3. Names of all States in india.

# In[45]:


exp_data['State'].nunique()


# In[49]:


#shows in countplot
sns.countplot(exp_data['State'])
sns.set_theme(style="darkgrid")
plt.xticks(rotation=90)


# Insights: If we ignore 31 text,  its Clearly shown there are 31 counts of states and union territories in India. 

# 4. Which is the Highest invested category of expenditure on which state?

# In[50]:


exp_data['Exp Category'].describe(include=all)


# In[51]:


exp_data.groupby("Exp Category")["State"].agg(pd.Series.mode)


# *Aggregate_Expenditure is Highest invested category of expenditure on Andhra Pradesh.
# 
# 
# Insights: Aggregate_Expenditure is Highest invested category of expenditure on Andhra Pradesh .

# 5.  Top 5 state having aggregate expenditure spending?

# In[52]:


exp_data.groupby(['Exp Category','State']).count()["value"]


# Insights: The Aggregate expenditure spending on these top 5 states are Andhra Pradesh, Arunachal Pradesh ,Assam ,Bihar & Chhattisgarh .

# 6. Expenditure spending over the years

# In[53]:


exp_data.Year.value_counts().to_frame('value')


# In[55]:


sns.countplot(x=exp_data['Year'],orient='v')
plt.xticks(rotation=90)
sns.set(rc={'figure.figsize':(30,30)})


# * Anual progress of expenditure.

# 6. Conclusion:
# In this way, I collect expenditure dataset fron Niti Aayog website.Load,clean and perform data analysis
# by using Exploratory data analysis in Python.I using python libraries such as pandas ,numpy,matplotlib,seaborn
# and pandas_profiling.For visualization using heatmap, counplot and graphs. In this EDA We extracted clean dataset
# as expenditure1 in csv for using for Data visualization.
