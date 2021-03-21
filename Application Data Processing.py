#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import xlrd


# In[31]:


DF_TotalAppsBySchool = pd.DataFrame()
startYear = 2006
for offset in range(0, 15):
    date = str(startYear+offset)+"-"+str(startYear+offset+1)
    path = r"data/application_data_by_school/" + date + "-app-data-by-school.xls"
    DF_TotalAppsAwardYearData = pd.read_excel(path, header = 5)
    DF_TotalAppsAwardYearData.drop(['Dependent Students', 'Independent Students', 'Quarterly Total'], axis=1, inplace=True)
    DF_TotalAppsAwardYearData['Award Year'] = date
    DF_TotalAppsAwardYearData.rename(columns = {
        'School': 'School Name',
        'Dependent Students.1':'Dependent Students', 
        'Independent Students.1':'Independent Students', 
        'Award Year To Date Total':'Total Applications YTD'
        }, inplace = True)
    DF_TotalAppsBySchool = DF_TotalAppsBySchool.append(DF_TotalAppsAwardYearData)

DF_TotalAppsBySchool['School Name'] = DF_TotalAppsBySchool['School Name'].str.strip()


# In[34]:


DF_TotalAppsBySchool.to_pickle("data/processed/application_data_by_school.pkl")


# In[32]:


DF_TotalAppsBySchool


# In[27]:


DF_plot = pd.DataFrame()
DF_plot['Award Year'] = DF_TotalAppsBySchool['Award Year'].unique()
DF_plot = DF_plot.set_index('Award Year')

for school in DF_TotalAppsBySchool['School Name'].unique()[1:20]:
    DF_school = DF_TotalAppsBySchool[DF_TotalAppsBySchool['School Name'] == school]
    DF_school = DF_school[['Total Applications YTD','Award Year']]
    DF_school = DF_school.set_index('Award Year').T.T
    DF_school.rename(columns = {'Total Applications YTD':school}, inplace=True)
    DF_plot = DF_plot.join(DF_school)


# In[28]:


plot = DF_plot.plot()
plot.legend(bbox_to_anchor=(1, 1))
plot.tick_params(axis='x', which='major', labelsize=10, labelrotation=90)


# In[ ]:




