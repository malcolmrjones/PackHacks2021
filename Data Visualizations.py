#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[27]:


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


# In[76]:


DF_IDs = pd.read_csv('data/OPEID_IPEDS.csv')
DF_IDs.set_index('UNITID', inplace=True)
pd.to_numeric(DF_IDs['OPEID'])
DF_IDs


# In[3]:


DF_Applications_Data = pd.read_pickle("data/processed/application_data_by_school.pkl")


# In[6]:


demographic_data = []
year = 2010
for offset in range(0, 10):
    demographic_of_year = pd.read_pickle(f"data/processed/{year+offset}_enrollment_data_by_school.pkl")
    demographic_data.append(demographic_of_year)


# In[14]:


DF_Applications_Data.groupby(['State']).sum().sort_values(by=['Total Applications YTD'], ascending=False)


# In[32]:


demographic_data[9].columns


# In[46]:


vis_demographics = demographic_data[9][['UNITID'] + demographics]
vis_demographics.set_index('UNITID', inplace=True)
vis_demographics


# In[83]:


vis_applications = DF_Applications_Data[DF_Applications_Data['Award Year'] == '2019-2020'][['OPE ID', 'School Name', 'Total Applications YTD', 'Award Year']]
vis_applications = vis_applications[vis_applications['OPE ID'] != "        "]
vis_applications['OPE ID'] = pd.to_numeric(vis_applications['OPE ID'])
vis_applications.rename(columns = {'OPE ID':'OPEID'}, inplace=True)
vis_applications.set_index('OPEID', inplace=True)
vis_applications


# In[84]:


# mergedDf = empDfObj.merge(salaryDfObj, left_index=True, right_index=True)
data_merge = DF_IDs.merge(vis_demographics, left_index=True, right_index=True)
data_merge = data_merge.merge(vis_applications, on='OPEID')
data_merge


# In[90]:


data_merge.sort_values('Total Applications YTD', ascending=False)[0:1000]


# In[ ]:




