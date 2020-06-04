# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:34:25 2020

@author: Robert Schuldt

ACS pull for additional research in racial disparities in access to 
health insurance in the state of arkansas following the ACA expansion.


"""
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

cols = {
    "NAME": "name",
    "B27001A_008E": "Total_White_19_25",
    "B27001A_009E": "Total_White_Insur_19_25",
    "B27001A_010E": "Total_White_UnInsur_19_25",
    "B27001A_011E": "Total_White_26_34",
    "B27001A_012E": "Total_White_Insur_26_34",
    "B27001A_013E": "Total_White_UnInsur_26_34",
    "B27001A_014E": "Total_White_35_44",
    "B27001A_015E": "Total_White_Insur_35_44",
    "B27001A_016E": "Total_White_UnInsur_35_44",
    "B27001A_017E": "Total_White_45_54",
    "B27001A_018E": "Total_White_Insur_45_54",
    "B27001A_019E": "Total_White_UnInsur_45_54",
    "B27001A_020E": "Total_White_55_64",
    "B27001A_021E": "Total_White_Insur_55_64",
    "B27001B_008E": "Total_AA_19_25",
    "B27001B_009E": "Total_AA_Insur_19_25",
    "B27001B_010E": "Total_AA_UnInsur_19_25",
    "B27001B_011E": "Total_AA_26_34",
    "B27001B_012E": "Total_AA_Insur_26_34",
    "B27001B_013E": "Total_AA_UnInsur_26_34",
    "B27001B_014E": "Total_AA_35_44",
    "B27001B_015E": "Total_AA_Insur_35_44",
    "B27001B_016E": "Total_AA_UnInsur_35_44",
    "B27001B_017E": "Total_AA_45_54",
    "B27001B_018E": "Total_AA_Insur_45_54",
    "B27001B_019E": "Total_AA_UnInsur_45_54",
    "B27001B_020E": "Total_AA_55_64",
    "B27001B_021E": "Total_AA_Insur_55_64",
}

vars_list = cols.keys()

print("This is my list of Dict keys ", vars_list )

var_param = ",".join(vars_list)
 #Creating a list of the actual variable names that we are interested in 

def acs_pull(word):
    ''' Identifying the variable I am interested in regarding African American 
        insurance rates this function grabs from a specified year and appends to an existing dataframe '''

    api = "https://api.census.gov/data/"+ str(word)+"/acs/acs1?get="+str(var_param)+"&for=state:05&key=6c64ce11724c4ffd70820041d4f49a8daf53e4b4"

    print(api)

    print('Requesting data from the American Communities Survey API')
    
    acs_data = requests.get(api)

    if (acs_data.status_code != 200):
        print('Error detected receiving (status code: ' + str(acs_data.status_code) + ')' )
    else:
        print('Sucessful request from American Communities Survey')
    
    content = acs_data.json()
    print(content)
    
    
    # print("Data converted to JSON formatting from ACS")
    cols['state'] = "05"

    #I am adding the list of headers that will actually define what the different variables are

    df= pd.DataFrame(data=content, columns = cols.values())
    df['Year']=word
    
    insur= df.drop([0])
    
    print('Pandas dataframe created at ' + str(ts))
    
    if not os.path.isfile('Z:\\DATA\\Urban League Project\\Data\\insurancedata.csv'):
        insur.to_csv('Z:\\DATA\\Urban League Project\\Data\\insurancedata.csv', index= True, header='headers')
    else:
        insur.to_csv('Z:\\DATA\\Urban League Project\\Data\\insurancedata.csv', mode= 'a' , header=False )
    print('Appended csv with year ' + str(word) +' to main file at ' + str(ts))


acs_pull(2017)
acs_pull(2016)
acs_pull(2015)
acs_pull(2014)
acs_pull(2013)
acs_pull(2012)
acs_pull(2011)
