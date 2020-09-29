#!/usr/bin/env python
# coding: utf-8

# ## Import libraries and dependencies

# In[1]:


import os
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd
import hvplot.pandas
#import seaborn as sns
import numpy as np
import plotly.express as px
#import matplotlib.pyplot as plt
import panel as pn
from panel.interact import interact
import holoviews as hv
hv.extension('bokeh')
pn.extension('plotly')


#get_ipython().run_line_magic('matplotlib', 'inline')


# ## Read in stock data and add new header with column names

# In[2]:


# Read in stock data and add new header with column names
one_mo_returns = pd.read_csv(Path("Resources/stocks_1month_returns.csv"), 
     names=["Null", "Ticker","Company Name", "Current Price", "Null2", "1 Month Price", "1 Mth Growth"])
six_mo_returns = pd.read_csv(Path("Resources/stocks_6month_returns.csv"), 
     names=["Null", "Ticker","Company Name", "Current Price", "Null2", "6 Month Price", "6 Mth Growth"])
one_yr_returns = pd.read_csv(Path("Resources/stocks_1yr_returns.csv"), 
     names=["Null", "Ticker","Company Name", "Current Price", "Null2", "1 Year Price", "1 Yr Growth"])
five_yr_returns = pd.read_csv(Path("Resources/stocks_5yr_returns.csv"), 
     names=["Null", "Ticker","Company Name", "Current Price", "5 Year Price", "Null2", "5 Yr Growth"])
sp500_returns = pd.read_csv(Path("Resources/index_sp500_returns.csv"))
sp500_sectors = pd.read_csv(Path("Resources/sp500_sectors.csv"))

# View data head
five_yr_returns.head()


# ## Rename columns in sp500_returns to match other dataframes

# In[3]:


# Rename columns in sp500_returns to match other dataframes
sp500_returns = sp500_returns.rename(columns={"Ticker": "Ticker", "Name": "Company Name", "Current Price": "Current Price", "1month": "1 Month Price", "1mth growth": "1 Mth Growth", "6month": "6 Month Price","6mth growth": "6 Mth Growth", "1year": "1 Year Price", "1 yr growth": "1 Yr Growth", "5year": "5 Year Price", "5 yr growth": "5 Yr Growth"})
sp500_returns.head()


# ## Insert Sector and Russell Sector Weight Columns in sp500_returns

# In[4]:


# Insert Sector and Russell Sector Weight Columns in sp500_returns
sp500_returns.insert(1, "Russell Sector", 'SP500')
sp500_returns.head()


# In[5]:


sp500_returns.insert(2, "Sector Weight", '100.00%')
sp500_returns.head()


# ## Rename columns in sp500_sectors to match other dataframes

# In[6]:


# Rename columns in sp500_sectors to match other dataframes
col_names = ["Company Name", "Ticker", "Sector Weight", "Russell Sector", "Zacks G Sector"]
sp500_sectors.columns = col_names
sp500_sectors.head()


# ## Reorder columns in sp500_sectors to match other dataframes

# In[7]:


# Reorder columns in sp500_sectors to match other dataframes
sp500_sectors = sp500_sectors[['Company Name', 'Ticker', 'Russell Sector', 'Sector Weight', 'Zacks G Sector']]
sp500_sectors.head()


# ## Delete empty columns and unnecessary columns

# In[8]:


# Delete empty columns and unnecessary columns
one_month = one_mo_returns.drop(columns=["Null", "Null2"])
six_month = six_mo_returns.drop(columns=["Null", "Company Name", "Current Price", "Null2"])
one_year = one_yr_returns.drop(columns=["Null", "Company Name", "Current Price", "Null2"])
five_year = five_yr_returns.drop(columns=["Null", "Company Name", "Current Price", "Null2"])
sp500 = sp500_returns.drop(columns=["3year", "3 yr growth"])
sectors = sp500_sectors.drop(columns=["Company Name", "Zacks G Sector"])
five_year.head()


# ## Drop Nulls

# In[9]:


# Drop Nulls
one_month.dropna(inplace=True)
six_month.dropna(inplace=True)
one_year.dropna(inplace=True)
five_year.dropna(inplace=True)
sp500.dropna(inplace=True)
sectors.dropna(inplace=True)

six_month.head()


# ## Set Ticker column as Index

# In[10]:


# Set Ticker column as Index
one_month.set_index('Ticker', inplace=True)
six_month.set_index('Ticker', inplace=True)
one_year.set_index('Ticker', inplace=True)
five_year.set_index('Ticker', inplace=True)
sp500.set_index('Ticker', inplace=True)
sectors.set_index('Ticker', inplace=True)
six_month.head()


# ## Combine Stocks dataframes and Sectors dataframe using columns as axis

# In[11]:


# Combine Stocks dataframes and Sectors dataframe using columns as axis
combined_stocks = pd.concat([sectors, one_month, six_month, one_year, five_year], axis="columns", join="inner", sort=False)
combined_stocks.fillna(0, inplace=True)
combined_stocks.sort_values(by=['Current Price'], inplace=True, ascending=False)
combined_stocks.head()


# ## Combine sp500 data with combined stocks and sectors dataframe using rows as axis

# In[12]:


# Combine sp500 data with combined stocks and sectors dataframe using rows as axis
combo_stocks_sp500 = pd.concat([combined_stocks, sp500], axis="rows", join="inner", sort=False)
combo_stocks_sp500.sort_values(by=['Current Price'], inplace=True, ascending=False)
combo_stocks_sp500.head()


# ## Remove % symbol from column values

# In[13]:


# Remove % symbol from column values
combo_stocks_sp500['Sector Weight'] = list(map(lambda x: x[:-1], combo_stocks_sp500['Sector Weight'].values))
combo_stocks_sp500['1 Mth Growth'] = list(map(lambda x: x[:-1], combo_stocks_sp500['1 Mth Growth'].values))
combo_stocks_sp500['6 Mth Growth'] = list(map(lambda x: x[:-1], combo_stocks_sp500['6 Mth Growth'].values))
combo_stocks_sp500['1 Yr Growth'] = list(map(lambda x: x[:-1], combo_stocks_sp500['1 Yr Growth'].values))
combo_stocks_sp500['5 Yr Growth'] = list(map(lambda x: x[:-1], combo_stocks_sp500['5 Yr Growth'].values))


# ## Convert string values to numeric values

# In[14]:


# Convert string values to numeric values
combo_stocks_sp500['Sector Weight'] = [float(x) for x in combo_stocks_sp500['Sector Weight'].values]
combo_stocks_sp500['1 Mth Growth'] = [float(x) for x in combo_stocks_sp500['1 Mth Growth'].values]
combo_stocks_sp500['6 Mth Growth'] = [float(x) for x in combo_stocks_sp500['6 Mth Growth'].values]
combo_stocks_sp500['1 Yr Growth'] = [float(x) for x in combo_stocks_sp500['1 Yr Growth'].values]
combo_stocks_sp500['5 Yr Growth'] = [float(x) for x in combo_stocks_sp500['5 Yr Growth'].values]
combo_stocks_sp500.head()


# ## Create a dataframe without the S&P 500

# In[15]:


# Create a dataframe without the S&P 500
combo_stocks = combo_stocks_sp500.drop(index='INX')
combo_stocks.head()


# ## Group stocks by sector

# In[16]:


# Group stocks by sector
stocks_sector = combo_stocks.groupby('Russell Sector').sum()
stocks_sector.head()


# ## Count stocks per sector

# In[17]:


# Count stocks per sector
sector_count = combo_stocks.groupby('Russell Sector').count()
sector_count.head()


# ## Calculate sector growth by time period and convert series objects to dataframes

# In[18]:


# Calculate sector growth by time period and convert series objects to dataframes
sector_growth1mo = pd.DataFrame({'Sector Growth': ((stocks_sector['1 Mth Growth'] / sector_count['1 Mth Growth']))})
sector_growth6mo = pd.DataFrame({'Sector Growth': ((stocks_sector['6 Mth Growth'] / sector_count['6 Mth Growth']))})
sector_growth1yr = pd.DataFrame({'Sector Growth': ((stocks_sector['1 Yr Growth'] / sector_count['1 Yr Growth']))})
sector_growth5yr = pd.DataFrame({'Sector Growth': ((stocks_sector['5 Yr Growth'] / sector_count['5 Yr Growth']))})
sector_growth5yr


# ## Reset dataframe indexes to set Sector categories as column values

# In[19]:


# Reset dataframe indexes to set Sector categories as column values
sector_growth1mo = sector_growth1mo.reset_index()
sector_growth6mo = sector_growth6mo.reset_index()
sector_growth1yr = sector_growth1yr.reset_index()
sector_growth5yr = sector_growth5yr.reset_index()
sector_growth5yr


# ## Plot sector growth data

# In[20]:


# Plot sector growth data
sector_growth5yr.hvplot.barh(
    x='Russell Sector',
    y='Sector Growth',
    title='5 Year Growth by Russell 3000 Sector',
    fontsize=(14),
    width=700,
    height=500,
    xformatter='%.0f %%')


# ## Define Sector Growth panel visualization functions

# In[21]:


# Define Sector Growth panel visualization functions
def get_sector1mo():
    """1 Month Growth by Russell 3000 Sector"""
    sector1mo = sector_growth1mo.hvplot.barh(
    x='Russell Sector',
    y='Sector Growth',
    title='1 Month Growth by Russell 3000 Sector',
    fontsize=(14),
    width=700,
    height=500,
    xformatter='%.1f %%')
    return sector1mo


# In[22]:


def get_sector6mo():
    """6 Month Growth by Russell 3000 Sector"""
    sector6mo = sector_growth6mo.hvplot.barh(
    x='Russell Sector',
    y='Sector Growth',
    title='6 Month Growth by Russell 3000 Sector',
    fontsize=(14),
    width=700,
    height=500,
    xlim=(0, 60),
    xformatter='%.0f %%')
    return sector6mo


# In[23]:


def get_sector1yr():
    """1 Year Growth by Russell 3000 Sector"""
    sector1yr = sector_growth1yr.hvplot.barh(
    x='Russell Sector',
    y='Sector Growth',
    title='1 Year Growth by Russell 3000 Sector',
    fontsize=(14),
    width=700,
    height=500,
    xformatter='%.0f %%')
    return sector1yr


# In[24]:


def get_sector5yr():
    """5 Year Growth by Russell 3000 Sector"""
    sector5yr = sector_growth5yr.hvplot.barh(
    x='Russell Sector',
    y='Sector Growth',
    title='5 Year Growth by Russell 3000 Sector',
    fontsize=(14),
    width=700,
    height=500,
    xformatter='%.0f %%')
    return sector5yr


# ## Define Top 10 Growth Stocks per time period

# In[25]:


# Define Top 10 Growth Stocks per time period
top10_1mo = combo_stocks.nlargest(10, '1 Mth Growth')
top10_1mo.sort_values(by=['1 Mth Growth'], ascending=True, inplace=True)
top10_6mo = combo_stocks.nlargest(10, '6 Mth Growth')
top10_6mo.sort_values(by=['6 Mth Growth'], ascending=True, inplace=True)
top10_1yr = combo_stocks.nlargest(10, '1 Yr Growth')
top10_1yr.sort_values(by=['1 Yr Growth'], ascending=True, inplace=True)
top10_5yr = combo_stocks.nlargest(10, '5 Yr Growth')
top10_5yr.sort_values(by=['5 Yr Growth'], ascending=True, inplace=True)
top10_5yr


# ## Generate plots for Top 10 growth stocks per time period

# In[26]:


# Generate plots for Top 10 growth stocks per time period
top10_5yr.hvplot.barh(
    x='Company Name', y='5 Yr Growth',
    title="Top 10 Growth Stocks in the Past 5 Years",
    width=900, height=400,
    xlabel='Company Name', ylabel='Growth per Stock',
    xlim=(0, 30),
    xformatter='%.0f %%')


# ## Define Stock Growth panel visualization functions

# In[27]:


# Define Stock Growth panel visualization functions
def get_top_1mo():
    top_1mo = top10_1mo.hvplot.barh(
    x='Company Name', y='1 Mth Growth',
    title="Top 10 Growth Stocks in the Past 1 Month",
    width=900, height=400,
    xlabel='Company Name', ylabel='Growth per Stock',
    xlim=(0, 30),
    xformatter='%.0f %%')
    return top_1mo


# In[28]:


def get_top_6mo():
    top_6mo = top10_6mo.hvplot.barh(
    x='Company Name', y='6 Mth Growth',
    title="Top 10 Growth Stocks in the Past 6 Months",
    width=900, height=400,
    xlabel='Company Name', ylabel='Growth per Stock',
    xlim=(0, 30),
    xformatter='%.0f %%')
    return top_6mo


# In[29]:


def get_top_1yr():
    top_1yr = top10_1yr.hvplot.barh(
    x='Company Name', y='1 Yr Growth',
    title="Top 10 Growth Stocks in the Past 1 Year",
    width=900, height=400,
    xlabel='Company Name', ylabel='Growth per Stock',
    xlim=(0, 30),
    xformatter='%.0f %%')
    return top_1yr


# In[30]:


def get_top_5yr():
    top_5yr = top10_5yr.hvplot.barh(
    x='Company Name', y='5 Yr Growth',
    title="Top 10 Growth Stocks in the Past 5 Years",
    width=900, height=400,
    xlabel='Company Name', ylabel='Growth per Stock',
    xlim=(0, 30),
    xformatter='%.0f %%')
    return top_5yr


# ## Create Rows with Sector and Stock Growth by Time Period

# In[31]:


# Create Rows with Sector and Stock Growth by Time Period
sectors_stocks_1mo = pn.Row(
    "##Sector Growth and Top 10 Growing Stocks in the Past 1 Month",
    get_sector1mo())
sectors_stocks_1mo.append(get_top_1mo())

# In[32]:


sectors_stocks_6mo = pn.Row(
    "##Sector Growth and Top 10 Growing Stocks in the Past 6 Months",
    get_sector6mo(),
    get_top_6mo()
)


# In[33]:


sectors_stocks_1yr = pn.Row(
    "##Sector Growth and Top 10 Growing Stocks in the Past 1 Year",
    get_sector1yr(),
    get_top_1yr()
)


# In[34]:


sectors_stocks_5yr = pn.Row(
    "##Sector Growth and Top 10 Growing Stocks in the Past 5 Years",
    get_sector5yr(),
    get_top_5yr()
)


# ## Create Tabs with Sector and Stock data arranged by Time Periods

# In[35]:


# Create Tabs with Sector and Stock data arranged by Time Periods
sectors_stocks_periods = pn.Tabs(
    ("1 Month", sectors_stocks_1mo),
    ("6 Months", sectors_stocks_6mo),
    ("1 Year", sectors_stocks_1yr),
    ("5 Years", sectors_stocks_5yr)
)


# In[36]:


sectors_stocks_periods.servable()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




