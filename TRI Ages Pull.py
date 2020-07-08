# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 17:19:09 2020

@author: Robert Schuldt

Grabbing data for Felix on this TRI assignment. 
"""


import datetime
import requests
import pandas as pd
import json
import os 

ts = datetime.datetime.now().isoformat()

cols_white = {
    "NAME": "name",
    "B01001A_003E": "W_White_under_5",
    "B01001A_004E": "W_White_5_9",
    "B01001A_005E": "W_White_10_14",
    "B01001A_006E": "W_White_15_17",
    "B01001A_007E": "W_White_18_19",
    "B01001A_008E": "W_White_20_24",
    "B01001A_009E": "W_White_25_29",
    "B01001A_010E": "W_White_30_34",
    "B01001A_011E": "W_White_35-44",
    "B01001A_012E": "W_White_45-54",
    "B01001A_013E": "W_White_55_64",
    "B01001A_014E": "W_White_65_74",
    "B01001A_015E": "W_White_75_84",
    "B01001A_016E": "W_White_85_Over",
    "B01001A_018E": "W_White_under_5",
    "B01001A_019E": "W_White_5_9",
    "B01001A_020E": "W_White_10_14",
    "B01001A_021E": "W_White_15_17",
    "B01001A_022E": "W_White_18_19",
    "B01001A_023E": "W_White_20_24",
    "B01001A_024E": "W_White_25_29",
    "B01001A_025E": "W_White_30_34",
    "B01001A_026E": "W_White_35-44",
    "B01001A_027E": "W_White_45-54",
    "B01001A_028E": "W_White_55_64",
    "B01001A_029E": "W_White_65_74",
    "B01001A_030E": "W_White_75_84",
    "B01001A_031E": "W_White_85_Over",
    }
cols_black = {
    "NAME": "name",
    "B01001B_003E": "Bm_under_5",
    "B01001B_004E": "BM_5_9",
    "B01001B_005E": "BM_10_14",
    "B01001B_006E": "BM_15_17",
    "B01001B_007E": "BM_18_19",
    "B01001B_008E": "BM_20_24",
    "B01001B_009E": "BM_25_29",
    "B01001B_010E": "BM_30_34",
    "B01001B_011E": "BM_35-44",
    "B01001B_012E": "BM_45-54",
    "B01001B_013E": "BM_55_64",
    "B01001B_014E": "BM_65_74",
    "B01001B_015E": "BM_75_84",
    "B01001B_016E": "BM_85_Over",
    "B01001B_018E": "BW_under_5",
    "B01001B_019E": "BW_5_9",
    "B01001B_020E": "BW_10_14",
    "B01001B_021E": "BW_15_17",
    "B01001B_022E": "BW_18_19",
    "B01001B_023E": "BW_20_24",
    "B01001B_024E": "BW_25_29",
    "B01001B_025E": "BW_30_34",
    "B01001B_026E": "BW_35-44",
    "B01001B_027E": "BW_45-54",
    "B01001B_028E": "BW_55_64",
    "B01001B_029E": "BW_65_74",
    "B01001B_030E": "BW_75_84",
    "B01001B_031E": "BW_85_Over",
    }
cols_american_indian = {
    "NAME": "name",
    "B01001C_003E": "AI_under_5",
    "B01001C_004E": "AI_5_9",
    "B01001C_005E": "AI_10_14",
    "B01001C_006E": "AI_15_17",
    "B01001C_007E": "AI_18_19",
    "B01001C_008E": "AI_20_24",
    "B01001C_009E": "AI_25_29",
    "B01001C_010E": "AI_30_34",
    "B01001C_011E": "AI_35-44",
    "B01001C_012E": "AI_45-54",
    "B01001C_013E": "AI_55_64",
    "B01001C_014E": "AI_65_74",
    "B01001C_015E": "AI_75_84",
    "B01001C_016E": "AI_85_Over",
    "B01001C_018E": "AIW_under_5",
    "B01001C_019E": "AIW_5_9",
    "B01001C_020E": "AIW_10_14",
    "B01001C_021E": "AIW_15_17",
    "B01001C_022E": "AIW_18_19",
    "B01001C_023E": "AIW_20_24",
    "B01001C_024E": "AIW_25_29",
    "B01001C_025E": "AIW_30_34",
    "B01001C_026E": "AIW_35-44",
    "B01001C_027E": "AIW_45-54",
    "B01001C_028E": "AIW_55_64",
    "B01001C_029E": "AIW_65_74",
    "B01001C_030E": "AIW_75_84",
    "B01001C_031E": "AIW_85_Over",
    }
cols_asian = {
    "NAME": "name",
    "B01001D_003E": "ASM_under_5",
    "B01001D_004E": "ASM_5_9",
    "B01001D_005E": "ASM_10_14",
    "B01001D_006E": "ASM_15_17",
    "B01001D_007E": "ASM_18_19",
    "B01001D_008E": "ASM_20_24",
    "B01001D_009E": "ASM_25_29",
    "B01001D_010E": "ASM_30_34",
    "B01001D_011E": "ASM_35-44",
    "B01001D_012E": "ASM_45-54",
    "B01001D_013E": "ASM_55_64",
    "B01001D_014E": "ASM_65_74",
    "B01001D_015E": "ASM_75_84",
    "B01001D_016E": "ASM_85_Over",
    "B01001D_018E": "ASW_under_5",
    "B01001D_019E": "ASW_5_9",
    "B01001D_020E": "ASW_10_14",
    "B01001D_021E": "ASW_15_17",
    "B01001D_022E": "ASW_18_19",
    "B01001D_023E": "ASW_20_24",
    "B01001D_024E": "ASW_25_29",
    "B01001D_025E": "ASW_30_34",
    "B01001D_026E": "ASW_35-44",
    "B01001D_027E": "ASW_45-54",
    "B01001D_028E": "ASW_55_64",
    "B01001D_029E": "ASW_65_74",
    "B01001D_030E": "ASW_75_84",
    "B01001D_031E": "ASW_85_Over",
    }
cols_pacific = {
    "NAME": "name",
    "B01001E_003E": "PIM_under_5",
    "B01001E_004E": "PIM_5_9",
    "B01001E_005E": "PIM_10_14",
    "B01001E_006E": "PIM_15_17",
    "B01001E_007E": "PIM_18_19",
    "B01001E_008E": "PIM_20_24",
    "B01001E_009E": "PIM_25_29",
    "B01001E_010E": "PIM_30_34",
    "B01001E_011E": "PIM_35-44",
    "B01001E_012E": "PIM_45-54",
    "B01001E_013E": "PIM_55_64",
    "B01001E_014E": "PIM_65_74",
    "B01001E_015E": "PIM_75_84",
    "B01001E_016E": "PIM_85_Over",
    "B01001E_018E": "PIW_under_5",
    "B01001E_019E": "PIW_5_9",
    "B01001E_020E": "PIW_10_14",
    "B01001E_021E": "PIW_15_17",
    "B01001E_022E": "PIW_18_19",
    "B01001E_023E": "PIW_20_24",
    "B01001E_024E": "PIW_25_29",
    "B01001E_025E": "PIW_30_34",
    "B01001E_026E": "PIW_35-44",
    "B01001E_027E": "PIW_45-54",
    "B01001E_028E": "PIW_55_64",
    "B01001E_029E": "PIW_65_74",
    "B01001E_030E": "PIW_75_84",
    "B01001E_031E": "PIW_85_Over",
    }
cols_other = {
    "NAME": "name",
    "B01001F_003E": "OTM_under_5",
    "B01001F_004E": "OTM_5_9",
    "B01001F_005E": "OTM_10_14",
    "B01001F_006E": "OTM_15_17",
    "B01001F_007E": "OTM_18_19",
    "B01001F_008E": "OTM_20_24",
    "B01001F_009E": "OTM_25_29",
    "B01001F_010E": "OTM_30_34",
    "B01001F_011E": "OTM_35-44",
    "B01001F_012E": "OTM_45-54",
    "B01001F_013E": "OTM_55_64",
    "B01001F_014E": "OTM_65_74",
    "B01001F_015E": "OTM_75_84",
    "B01001F_016E": "OTM_85_Over",
    "B01001F_018E": "OTW_under_5",
    "B01001F_019E": "OTW_5_9",
    "B01001F_020E": "OTW_10_14",
    "B01001F_021E": "OTW_15_17",
    "B01001F_022E": "OTW_18_19",
    "B01001F_023E": "OTW_20_24",
    "B01001F_024E": "OTW_25_29",
    "B01001F_025E": "OTW_30_34",
    "B01001F_026E": "OTW_35-44",
    "B01001F_027E": "OTW_45-54",
    "B01001F_028E": "OTW_55_64",
    "B01001F_029E": "OTW_65_74",
    "B01001F_030E": "OTW_75_84",
    "B01001F_031E": "OTW_85_Over",
}


def acs_pull(word, cols):
    ''' Identifying the variable I am interested in regarding African American 
        insurance rates this function grabs from a specified year and appends to an existing dataframe '''
    
    vars_list = cols.keys()
    print("This is my list of Dict keys ", vars_list )
    var_param = ",".join(vars_list)
    #Creating a list of the actual variable names that we are interested in 
    
    api = "https://api.census.gov/data/"+ str(word)+"/acs/acs5?get="+str(var_param)+"&for=state:05&key=6c64ce11724c4ffd70820041d4f49a8daf53e4b4"
    


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
    
    if not os.path.isfile('C:\\Users\\3043340\\Documents\TRI\\age_estimates.csv'):
        insur.to_csv('C:\\Users\\3043340\\Documents\TRI\\age_estimates.csv', index= True, header='headers')
    else:
        insur.to_csv('C:\\Users\\3043340\\Documents\TRI\\age_estimates.csv', mode= 'a' , header='header' )
    print('Appended csv with year ' + str(word) +' to main file at ' + str(ts))


acs_pull(2018, cols_white )
acs_pull(2018, cols_black )
acs_pull(2018, cols_asian )
acs_pull(2018, cols_american_indian )
acs_pull(2018, cols_pacific )
acs_pull(2018, cols_other )

