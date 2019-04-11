# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:45:54 2019

@author: robsc
"""


import datetime
import requests
import pandas as pd
import json
import os 

ts = datetime.datetime.now().isoformat()



 #Creating a list of the actual variable names that we are interested in 

def acs_pull(word):
    ''' Identifying the variable I am interested in regarding African American 
        insurance rates this function grabs from a specified year and appends to an existing dataframe '''

    api = "https://api.census.gov/data/" + str(word)+ "/acs/acs1?get=NAME,B27001A_001E,B27001B_001E,B27001B_008E,B27001B_010E,B27001B_011E,B27001B_013E&for=county:*&in=state:05,48,40,20,29,47,28"

    print('Requesting data from the American Communities Survey API')
    
    acs_data = requests.get(api)

    if (acs_data.status_code != 200):
        print('Error detected receiving (status code: ' + str(acs_data.status_code) + ')' )
    else:
        print('Sucessful request from American Communities Survey')
    
    content = acs_data.json()
    print("Data converted to JSON formatting from ACS")
    headers= ['County_Name','Total_Whit_Est_Insur' ,'Total_AA_Est_Insur','Age19-25Insur-AA', 'Age19-25Non-AA', 'Age26-34Insur-AA',  'Age26-34Non-AA', 'fips_st', 'fips_cnty']

    #I am adding the list of headers that will actually define what the different variables are

    df= pd.DataFrame(data=content, columns = headers)
    df['Year']=word
    
    df.drop([0])
    
    print('Pandas dataframe created at ' + str(ts))
    
    if not os.path.isfile('C:\\Users\\robsc\\Desktop\\Github Desktop\\American-Communities-Survey\\insurancedata.csv'):
        df.to_csv('C:\\Users\\robsc\\Desktop\\Github Desktop\\American-Communities-Survey\\insurancedata.csv', mode= 'a' , header=headers )
    else:
        df.to_csv('C:\\Users\\robsc\\Desktop\\Github Desktop\\American-Communities-Survey\\insurancedata.csv', mode= 'a' , header=False )
    print('Appended csv with year ' + str(word) +' to main file at ' + str(ts))


acs_pull(2017)
acs_pull(2016)
acs_pull(2015)
acs_pull(2014)
acs_pull(2013)
acs_pull(2012)
acs_pull(2011)


