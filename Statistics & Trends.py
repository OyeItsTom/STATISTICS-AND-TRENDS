#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 22:07:20 2023

@author: tomthomas
"""

import pandas as pd

def read_data(filename):
    
    '''This function is used to access the csv dataset.'''
    #Read the csv file
    df = pd.read_csv(filename, skiprows = 4)
    #To return the data
    return df

def filter_data(df, col, value, country, year):
    
    '''
    This function is used to filter and transpose the dataset and return both datas.
 
    Parameters
    ----------
    df : The dataset received with the data_reading function()
    col : Column name
    value : Value in the selected column
    country : Selected countries
    years : Selected years
    
    Returns
    -------
    df1 : Filtered dataset
    df2 : Transposed dataset of df1 
    '''
    #Grouping the data with column
    df1 = df.groupby( col, group_keys= True)
    #Selecting a value in the grouped data
    df1 = df1.get_group(value)
    #Reseting the index
    df1 = df1.reset_index()
    #Set Country Name as the index
    df1.set_index('Country Name', inplace=True)
    #Filtering data by years
    df1 = df1.loc[:, year]
    #Filtering data by countries
    df1 = df1.loc[country, :]
    #Dropping the NA values
    df1= df1.dropna(axis = 1)
    #Reseting the index again
    df1 = df1.reset_index()
    #Set Country Name as the index to transpose
    df2 = df1.set_index('Country Name')  
    #Transpose the data
    df2 = df2.transpose()
    #Returning both data
    return df1,df2


#Calling the dataset
data =  read_data("Climate.csv")