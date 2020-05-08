#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
This is a workaround to scrape html tables from an NIC site listing agriculture commodities.
The site is aspx and rather than writing a spider, it was faster to save the pages offline and then import data.  
"""


# In[1]:


import pandas as pd


# In[10]:


#Reading a single html file using pandas and writing to a csv file

#url = 'C:/Users/rijo/MAD/BeautifulSoup/Date%20Wise%20Report.html'
#df = pd.concat(pd.read_html(url,attrs={'id':'_ctl0_content5_gv'}))
#df.to_csv('Scraped Datewise Report.csv')


# In[20]:


#Reading multiple html files using pandas and writing to a single csv file

urls = [
    'C:/Users/rijo/MAD/BeautifulSoup/Date%20Wise%20Report%20Jan2020.html',
    'C:/Users/rijo/MAD/BeautifulSoup/Date Wise Report Feb2020.html',
    'C:/Users/rijo/MAD/BeautifulSoup/Date Wise Report Mar2020.html'
    ]

df = pd.DataFrame(columns=[
    'Market', 'Date', 'Variety', 'Grade', 'Arrivals', 'Unit', 'Min', 'Max', 'Modal', 'District'])

for url in urls:
    table = pd.concat(pd.read_html(url,attrs={'id':'_ctl0_content5_gv'}))
    df = df.append(table)

df.to_csv('Scraped data from mulitple months.csv')

