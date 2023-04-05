#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 22:07:20 2023

@author: tomthomas
"""

import pandas as pd
import matplotlib.pyplot as plt

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

def bar_plot(data, title, x, y, a):
    
    '''
    This function is used for plotting bar graph
    
    Parameters
    ----------
    data : Filtered dataset from filter_data()
    title : Title name
    x : xlabel
    y : ylabel
    a : Xticks
    
    '''
    #To plot bar graph
    ax = data.plot.bar(x='Country Name', rot=0, figsize=(50,30), fontsize=50)
    #Setting yticks
    ax.set_yticks(a)
    #Setting title and fontsize
    ax.set_title(title, fontsize=50)
    #Setting xlabel and fontsize
    ax.set_xlabel(x, fontsize=50)
    #Setting ylabel and fontsize
    ax.set_ylabel(y, fontsize=50)
    ax.legend(fontsize=50)
    #saving bar graph as image
    plt.savefig(title + '.png')
    plt.show()
    #return statement is used at the the end of a function
    return

def line_plot(data, title, x, y, a):
    
    '''
    This function is used for plotting bar graph
    
    Parameters
    ----------
    data : Transposed dataset from filter_data()
    title : Title name
    x : xlabel
    y : ylabel
    a : Xticks
    
    '''
    #To plot line graph
    data.plot.line(figsize=(50,30), fontsize=36, linewidth=4.0)
    #Setting yticks
    plt.yticks(a)
    #Setting title and fontsize
    plt.title(title, fontsize=50)
    #Setting xlabel and fontsize
    plt.xlabel(x,fontsize=50)
    #Setting ylabel and fontsize
    plt.ylabel(y, fontsize=50)
    plt.legend(fontsize=50)
    #saving line graph as image
    plt.savefig(title + '.png')
    plt.show()
    #return statement is used at the the end of a function
    return

#Calling the dataset
data =  read_data("Climate.csv")


#Setting countries and years as list for bar graph
country1= ['Brazil','India','Mexico','Nepal','Uruguay']
year1 = ['1961', '1971', '1981', '1991', '2001','2011']
#Setting xticks values as list
x1 = [1000, 2000, 3000, 4000, 5000]
#calling filter_data() function and store the return values in data2 and data3
data2, data3 = filter_data(data, 'Indicator Name','Cereal yield (kg per hectare)',country1,year1)
#plotting bar graph with the filtered data in bar_plot() function
bar_plot(data2, 'Cereal yield', 'Countries', 'kg per hectare', x1)

#Setting countries and years as list for line graph
country2= ['Brazil', 'China', 'Mexico', 'Uruguay', 'Zimbabwe']
year2 = ['1971','1981','1991','2001','2011']
#Setting xticks values as list
x2 = [500,1000,1500,2000,2500,3000,3500]
#calling filter_data() function and store the return values in data4 and data5
data4, data5 = filter_data(data, 'Indicator Name','Electric power consumption (kWh per capita)',country2,year2)
#plotting line graph with the transposed data in line_plot() function
line_plot(data5, 'Electric power consumption', 'Year', 'kWh per capita', x2)


#Setting countries and xticks values as list for bar graph 
x3 = [20, 40, 60, 80, 100]
country3= ['Andorra','Austria','China','Korea, Rep.','Libya']
#calling filter_data() function and store the return values in data6 and data7
data6, data7 = filter_data(data, 'Indicator Name','Urban population (% of total population)',country3,year1)
#plotting bar graph with the filtered data in bar_plot() function
bar_plot(data6, 'Urban population ', 'Countries', '% of total population', x3)


country4= ['Bangladesh', 'Guyana', 'India','Kenya', 'Lesotho']
#calling filter_data() function and store the return values in data8 and data9
data8, data9 = filter_data(data, 'Indicator Name','Agriculture, forestry, and fishing, value added (% of GDP)',country4,year1)
#plotting line graph with the filtered data in line_plot() function
line_plot(data9, 'Agriculture, forestry, and fishing, value added', 'Year', '% of GDP', x3)














