#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


data_list = []
totals = [
        'UNITID',
        'EFALEVEL',
        'EFTOTLT'
]
demographics = [
        'EFTOTLM',
        'EFTOTLW',
        'EFAIANT',
        'EFASIAT',
        'EFBKAAT',
        'EFHISPT',
        'EFNHPIT',
        'EFWHITT',
        'EF2MORT',
        'EFUNKNT',
        'EFNRALT'
]


# In[6]:


year = 2009
for offset in range(0, 10):
    year += 1
    filepath = f'data/enrollment_data_by_school/ef{year}a.csv'
    DF_Enrollment_Data_Full = pd.read_csv(filepath)
    DF_Enrollment_Data = DF_Enrollment_Data_Full[totals + demographics]
    # Get the rows that tell us the undergrad total population of each university
    DF_Enrollment_Data = DF_Enrollment_Data[DF_Enrollment_Data['EFALEVEL'] == 2]
    DF_Enrollment_Data[demographics] = DF_Enrollment_Data.apply(lambda x: round((x[demographics] / x['EFTOTLT']) * 100, 0), axis=1)
    data_list.append(DF_Enrollment_Data)


# In[50]:


df = data_list[9].assign(EFBKAAT = lambda x: (round(x['EFBKAAT'] / x['EFTOTLT'] * 100, 0)))
df


# In[17]:


year = 2010
for offset in range(0, len(data_list)):
    data_list[x].to_pickle(f"data/processed/{year+offset}_enrollment_data_by_school.pkl")


# In[16]:





# In[ ]:




