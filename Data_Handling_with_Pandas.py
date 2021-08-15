# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:16:34 2019

@author: arpendu.ganguly
"""

##########################################################################################
#------------------------------------Pandas Tutorial-------------------------------------#
##########################################################################################
import numpy as np
import pandas as pd
import numpy as np
import os
# =============================================================================
# =============================================================================
# # 
# =============================================================================
# =============================================================================
##########################################################################################
#1. Object Creation in Pandas
##########################################################################################

#Creating a Data Series a Series by passing a list of values, letting pandas create a default integer index
A1 = pd.Series([2,10,4,"Amy",np.nan,7])
print(A1)

#Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns, sequence of Dates

dates = pd.date_range(start = '2020-01-01',periods =10, freq = "M")#Year, Month, Date
print(dates)
help(pd.date_range)


#Creating a DataFrame by passing a dict of objects that can be converted to series-like

A2= pd.DataFrame({'A':[1,2,3,4],
                  'B':pd.Timestamp('20190915'),
                  'C':np.array([4]*4,dtype = 'int64'),
                  'D':pd.Categorical(["test","train","test","train"]),
                  'E': 4.2})

#Creating an Empty DataFrame
Empty_Data = pd.DataFrame()

#Checking structure of Data
A2.dtypes

#Converting Pandas Object into a Numpy Object
###NumPy arrays have one dtype for the entire array, while pandas DataFrames have one dtype per column.
### When you call DataFrame.to_numpy(), pandas will find the NumPy dtype that can hold all of the dtypes in the DataFram


##########################################################################################
#2. Reading Data for further Analysis
##########################################################################################

#Setting the working directory
os.chdir('C:/Ganesha_Accenture/Ganesha_IVY/Python/01DATA_PROCESSING/01DATA')
os.chdir(R'C:\Ganesha_Accenture\Ganesha_IVY\Python\01DATA_PROCESSING\01DATA')

path_data = os.getcwd()
path_data

GoogleData = pd.read_csv("Googleplaystore_1.csv")

##########################################################################################
#3.Viewing Data
##########################################################################################

#Head of Data
GoogleData.head()

First_100=GoogleData.head(100)

#Tail of Data
GoogleData.tail()
Last_10=GoogleData.tail(10)


#Viewing the Columns of Data
GoogleData.columns

#Checking the Structure of Data
GoogleData.dtypes

#Summary of the Data
Des=GoogleData.describe()

#Including all the Data Levels
Des_all=GoogleData.describe(include='all')


# Print the shape of Data
print(GoogleData.shape)

# Print the info of Data
print(GoogleData.info())


##########################################################################################
#4.Changing the type of data
##########################################################################################

#Converting a coloumn to a particular Data Type
pd.to_numeric(GoogleData.Rating)

#Multiple Columns
GoogleData_1=GoogleData.copy()
GoogleData_1.dtypes
GoogleData_1["Rating"] = GoogleData_1["Rating"].apply(str)
GoogleData_1["Rating"] = GoogleData_1["Rating"].apply(float)
GoogleData_1.dtypes


##########################################################################################
#5.Selecting the Data
##########################################################################################


#Selecting only one Column 
GoogleData1= GoogleData[['App']]
GoogleData1= GoogleData.App

#Selecting only Multiple Columns
#Based on Labels
GoogleData2= GoogleData[['App','Category','Rating','Reviews']]


GoogleData2= GoogleData.loc[:,'App']

GoogleDat2= GoogleData.loc[200:300,['App','Size','Reviews']]


#Based on Index
GoogleData2= GoogleData.iloc[:,[2,3,10]]

#Selecting Multiple Rows
GoogleData2= GoogleData.iloc[0:3,:]

GoogleData2= GoogleData.iloc[0:3,3:10]


##########################################################################################
#6. Filtering the Data
##########################################################################################

GoogleData3 = GoogleData[GoogleData.Rating > 3]
GoogleData3 = GoogleData[GoogleData['Rating'] > 3]


#AND
GoogleData4 = GoogleData[(GoogleData.Rating > 3) & (GoogleData.Reviews > 10000 )]

#OR
GoogleData5 = GoogleData[(GoogleData.Rating > 3) | (GoogleData.Reviews > 10000 ) ]


#AND & OR
GoogleData5 = GoogleData[((GoogleData.Rating > 3) & (GoogleData.Reviews > 10000 )) | (GoogleData.Category == "ART_AND_DESIGN")]


GoogleData6 = GoogleData[GoogleData['Category'].isin(["ART_AND_DESIGN","HEALTH_AND_FITNESS"])]

#NOT
GoogleData4 = GoogleData[(GoogleData.Rating > 3) & ~(GoogleData.Reviews > 10000 )]

#MULITPLE NOT
GoogleData4 = GoogleData[~(GoogleData.Rating ==3) & ~(GoogleData.Reviews > 10000 )]


##########################################################################################
#7. Working with Missing Data
##########################################################################################
#pandas primarily uses the value np.nan to represent missing data

#Finding the columns with Missing Values
Miss = GoogleData.isnull().sum()

#Total Sum of Missing Values
GoogleData.isnull().sum().sum()

#Imputing Missing values withe particular value
GoogleData7=GoogleData.fillna(value=0)
Miss = print(GoogleData7.isnull().sum())

#Working with particular columns
GoogleData7=GoogleData
GoogleData7['Rating'] = GoogleData7['Rating'].fillna((GoogleData7['Rating'].mean()))


##########################################################################################
#8. Stats for the Variables
##########################################################################################


WHO = pd.read_csv("WHO.csv")
StatWHO=WHO.describe()

WHO.dtypes
WHO.Population.mean()
WHO['Population'].mean()
WHO.Population.median()
WHO.Population.sum()
WHO.Population.std()
WHO.Population.var()
WHO.Population.count()

##########################################################################################
#9. Merging for the Variables
##########################################################################################
#pandas has full-featured, high performance in-memory join operations idiomatically very similar to relational databases like SQL.

#Merge Methods
#left=Use keys from left frame only
#right=Use keys from right frame only
#outer=Use union of keys from both frames
#inner=Use intersection of keys from both frames


left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})


right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})

result = pd.merge(right,left, on='key')



#Based on Different Key Name
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

result = pd.merge(right, left, on=['key1', 'key2'])

result1=pd.merge(left,right,how='left',on=['key1','key2'])
result2=pd.merge(left,right,how='right',on=['key1','key2'])
result3=pd.merge(left,right,how='outer',on=['key1','key2'])
result4=pd.merge(left,right,how='inner',on=['key1','key2'])


##########################################################################################
#10. Grouping the Variables
##########################################################################################


#1 group
df=WHO.copy()
df2= df.groupby(['Region']).sum().reset_index()

df2= df.groupby(['Region']).sum().reset_index()

#Multiple Groups
df3= df.groupby(['Country','Region']).sum().reset_index()

#Multiple variables and Multiple Measures:
df4 = df.groupby(['Region']).agg({'Population':'sum',
                                  'Under15':'mean'}).reset_index()

#Sumif/Countif/Average if

df['Region_Pop']= df['Population']/df.groupby(['Region'])['Population'].transform('sum')

##########################################################################################
#11. Pivot Tables
##########################################################################################


#Reshaping
All_Region = WHO[['Country','Region','Population']]
#Europe = Europe[Europe.Region == "Europe"]

All_Region_1=All_Region.pivot(index='Region', columns='Country', values='Population').reset_index()

All_Region_1=All_Region_1.fillna(value=0)


#If the values argument is omitted, and the input DataFrame has more than one column of values which are not used as column or index inputs to pivot, then the resulting “pivoted” DataFrame will have hierarchical columns whose topmost level indicates the respective value column

#Melt
All_Region_2=All_Region_1.melt(id_vars=['Region'],var_name='Country_Name')
All_Region_2=All_Region_2[All_Region_2.value>0]
All_Region_2= All_Region_2.rename(columns = {"value":"Population"})


#Finding Summary Statistics for One Variable
Agg_1 = WHO.groupby('Region').agg({"Population": [min, max, sum, np.median,np.mean,np.var,np.std]}).reset_index() 

Stats = WHO.describe()
#Finding Summary Statistics for More than One Variable
Agg_2=pd.pivot_table(WHO, values=['Population','Under15'], index=['Region'], 
                     aggfunc={'Population':[np.mean,np.min,np.max],
                      'Under15':[np.mean,np.min]}).reset_index()


# =============================================================================
# Dropping Duplicates
# =============================================================================

# making data frame from csv file 
data = pd.read_csv("employees.csv") 
data_1 = data.copy()
# sorting by first name 
data_2 = data_1.sort_values("First Name",inplace = False, ascending = True)
data_1.sort_values("First Name",inplace = True, ascending = True)
                            
data_1.sort_values(["First Name","Salary"],inplace = True, ascending = [True,False]) 


#Subset takes a column or list of column label.
  
#keep: keep is to control how to consider duplicate value. It has only three distinct value and default is ‘first’.

#If ‘first’, it considers first value as unique and rest of the same values as duplicate.
#If ‘last’, it considers last value as unique and rest of the same values as duplicate.
#If False, it consider all of the same values as duplicates
#inplace: Boolean values, removes rows with duplicates if True.

#Return type: DataFrame with removed duplicate rows depending on Arguments passed
# dropping ALL duplicte values 
data_1.drop_duplicates(subset =["First Name","Gender"],
                     keep = 'first', inplace = True) 
  
# =============================================================================
# Control Structures
# =============================================================================

# =============================================================================
# If-Else
# =============================================================================
data2 = pd.read_csv("New_Employee.csv") 
data2.Age
data2['Age']
 
def Age_cat(y):
    if y>=20 and y<25 :
        return 'Between 20-25'
    elif y>=25 and y<30 :
        return 'Between 26-30'
    else:
        return 'Above 30'

#bucketting rating to a new column         
data2['Age_Cat'] = data2['Age'].apply(Age_cat)



# =============================================================================
# For - Loop 
# =============================================================================

# Iterating over a list 
print("List Iteration") 
l = ["Data Science", "is a ", "Great Subject!"] 
len(l)
l[0]
type(l)

for i in l: 
    #i=l[0]
    print(i) 
       
# Iterating over a tuple (immutable) 
print("/nTuple Iteration") 
t = ("Data Science", "is a ", "Great Subject!") 
for i in t: 
    print(i) 
       
# Iterating over a String 
print("/nString Iteration")     
s = "Data"
for i in s : 
    print(i) 
       
# Iterating over dictionary 
print("/nDictionary Iteration")    
d = dict()  
d['xyz'] = 123
d['abc'] = 345
for i in d : 
    print("%s-->%d" %(i, d[i]))
    

# Nested For Loops
for i in range(1, 6): 
    #i=3
    for j in range(i): 
        #j=1
        print(i, end=' ') 
        i+=1
    print() 
    
    
y=range(1, 6)
len(y)


# =============================================================================
# Working with different Data Types
# =============================================================================
import os
wd = os.getcwd()
os.listdir(wd)

os.chdir('C:/Ganesha_Accenture/ZSelf/Data_Scientist_with_Python')
os.getcwd()

# Open a file: file
file = open('sample.txt', mode='r')

#Storing the Contents
if file.mode == 'r':
    contents =file.read() 


   
# Check whether file is closed
print(file.closed)

# Close file
file.close()


# Check whether file is closed
print(file.closed)

# Read & print the first 3 lines
with open('sample.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    
    
# =============================================================================
# Reading Excel Files 
# =============================================================================
os.chdir('C:/Ganesha_Accenture/Ganesha_IVY/Python/01DATA_PROCESSING/01DATA')
path_data = os.getcwd()
path_data

import pandas as pd

# Assign spreadsheet filename: file
file = 'World_Bank_Population.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print(xls.sheet_names)
print(xls)

# Load a sheet into a DataFrame by name: df1
df1 = xls.parse('World_Bank_Population')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xls.parse(1)

# Print the head of the DataFrame df2
print(df2.head())

# Parse the first column of the second sheet and rename the column: df2
df3 = xls.parse(1, usecols=[0,1,2,3],skiprows=[0], names=['Country_New','A','B','C'])
df4 = xls.parse(1, usecols=[0,1,2,3], names=['Country_New','A','B','C'])
    

# =============================================================================
# Opening and reading flat files from the web
# =============================================================================
# Import packages
import pandas as pd

# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Read file into a DataFrame: df
df = pd.read_csv(url, sep=';')


# Print the head of the DataFrame
print(df.head())



# =============================================================================
# Turning a webpage into data using BeautifulSoup 
# =============================================================================

# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Get the title of Guido's webpage: guido_title
guido_title = soup.title
# Print the title of Guido's webpage to the shell
print(guido_title)

# Get Guido's text: guido_text
guido_text = soup.get_text()

# Print Guido's text to the shell
print(guido_text)