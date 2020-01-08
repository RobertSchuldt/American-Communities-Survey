# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:45:54 2019
@author: Robert Schuldt
@email: rschuldt@uams.edu
"""


import datetime
import requests
import pandas as pd
import json
import os 

ts = datetime.datetime.now().isoformat()

income = "B19013_001E"
education = "B15003_022E,B23025_004E,B01003_001E"
key1 = "6c64ce11724c4ffd70820041d4f49a8daf53e4b4"
 #Creating a list of the actual variable names that we are interested in 

def acs_pull(word):
    ''' Identifying the variable I am interested in regarding African American 
        insurance rates this function grabs from a specified year and appends to an existing dataframe '''

    #api = "https://api.census.gov/data/"+str(word)+"/acs/acs5?get=Name&for=zip%20code%20tabulation%20area:*&key=6c64ce11724c4ffd70820041d4f49a8daf53e4b4"
    api = "https://api.census.gov/data/"+str(word)+"/acs/acs5?get=NAME,"+str(income)+","+str(education)+"&for=zip%20code%20tabulation%20area:*&key=6c64ce11724c4ffd70820041d4f49a8daf53e4b4"

    print('Requesting data from the American Communities Survey API')
    
    acs_data = requests.get(api)

    if (acs_data.status_code != 200):
        print('Error detected receiving (status code: ' + str(acs_data.status_code) + ')' )
    else:
        print('Sucessful request from American Communities Survey')
    
    content = acs_data.json()
    print("Data converted to JSON formatting from ACS")
    headers= ['ID', 'Median Income','Education Level' ,'Employment Rate 16+', 'Totalpop', 'Ztca']
    #I am adding the list of headers that will actually define what the different variables are

    df= pd.DataFrame(data=content, columns = headers)
    df['Year']=word
    
    insur= df.drop([0])
    
    print('Pandas dataframe created at ' + str(ts))
    
    if not os.path.isfile('Z:\\DATA\\\HCBS Alz Near Poor\\ACS Pull\\nearpoor.csv'):
        insur.to_csv('Z:\\DATA\\HCBS Alz Near Poor\\ACS Pull\\nearpoor.csv', index= True, header='headers' )
    else:
        insur.to_csv('Z:\\DATA\\HCBS Alz Near Poor\\ACS Pull\\nearpoor.csv', mode= 'a' , header=False )
    print('Appended csv with year ' + str(word) +' to main file at ' + str(ts))


acs_pull(2015)
