

import datetime
import requests
import pandas as pd
import json

ts = datetime.datetime.now().isoformat()


''' Identifying the variable I am interested in regarding African American 
insurance rates '''

api = "https://api.census.gov/data/2017/acs/acs1?get=NAME,B27001A_001E,B27001B_001E,B27001B_008E,B27001B_010E,B27001B_011E,B27001B_013E&for=county:*&in=state:05,48,40,20,29,47,28"

print('Requesting data from the American Communities Survey API')
    
acs_data = requests.get(api)

if (acs_data.status_code != 200):
    print('Error detected receiving (status code: ' + str(acs_data.status_code) + ')' )
else:
    print('Sucessful request from American Communities Survey')
    
content = acs_data.json()
print("Data converted to JSON formatting from ACS")
#Creating a list of the actual variable names that we are interested in 
headers= ['County_Name','Total_Whit_Est' ,'Total_AA_Est','Age19-25Insur', 'Age19-25Non', 'Age26-34Insur',  'Age26-34Non', 'fips_st', 'fips_cnty']

#I am adding the list of headers that will actually define what the different variables are

df= pd.DataFrame(data= content, columns = headers)
print('Pandas dataframe created at ' + ts)

insure_data = df.drop([0])

