# -*- coding: utf-8 -*-

"""
Created on Wed Apr 10 13:02:11 2019

@author: Robert Schuldt

Use the ACS to pull in data by race and insurance coverage status for work
with the Urban league by accessing the API tools provided by the ACS via
census.gov
"""





import requests
import pandas as pd
import json




''' Identifying the variable I am interested in regarding African American 
insurance rates '''


api = "https://api.census.gov/data/2017/acs/acs1?get=NAME,B27001B_008E,B27001B_010E,B27001B_011E,B27001B_013E&for=county:*&in=state:05"

def acs_request(word, word2):
    ''' Function to call in the API data from ACS'''
    print('Requesting data from the American Communities Survey API')
    
    requests.get(word)
    
    if (word2.status_code == 200):
          print('Sucess pulling from American Communities Survey')
          quit()
        
    
    if (word2.status_code != 200):
          print('Error detected receiving (status code: ' + str(word2.status_code) + ')' )
          quit()
    

data = acs_request(api, 'acs_data')    




