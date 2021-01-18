import pandas as pd
import datetime
import numpy as np
import requests, json

# Google Maps distance api key
api_key ='INSERT API KEY'

# url variable store url  
url ='https://maps.googleapis.com/maps/api/distancematrix/json?'

## just kept a separate filtering method (by capacity)
def filter_by_capacity(icu_percentage, inpatient_percentage, data):
    return data[((data["percentage inpatient"]<inpatient_percentage) & (data["percentage inpatient"]>=0.0))|((data["percentage icu"]<icu_percentage) & (data["percentage icu"]>=0.0))]

#first filters by state, calculates and sorts the df by distance, then if you want, can filter by threshold icu inpatient
def filter_by_state_calc_distance(current_location, icu_percentage, inpatient_percentage, data):
    my_state=current_location[-2:]
    my_state = current_location.split(",")[-1].strip()[:2]
    state_df=data.query('state==@my_state') # can add filter for percentage in icu or inpatient

    print(state_df)
    
    i = 0
    for index, row in state_df.iterrows():
        if i > 10:
            break
        i += 1
        dest = row["address"]
        r = requests.get(url + 'origins = ' + current_location +
                    '&destinations = ' + dest +
                    '&key = ' + api_key) 
        dist = r.json()
        row["distance"] = dist
    state_df.sort_values(by=["distance"]) # sort dataframe by distance in ascending order-> can pick the k closest by then
    return filter_by_capacity(icu_percentage,inpatient_percentage,state_df)
    
#search by address STREET NAME, CITY, ZIP CODE
def access_data_by_name(address_name, data):
    split_addr=address_name.split(',')
    print(split_addr)
    length=len(split_addr)
    print(length)
    for word in split_addr:
        word=word.strip()
        word=word.upper()
        print(word)
    hosp_data=1
    hosp_ind=data[((data["address"]==split_addr[0])&(data["zip"]==float(split_addr[2])))].index
    if(len(hosp_ind)==0):
        print("No match\n")
        return ()
    print(hosp_ind)
    hosp_data=(data["percentage inpatient"][hosp_ind[0]],data["percentage icu"][hosp_ind[0]], data["distance"][hosp_ind[0]])
    return hosp_data

#returns the k closest hosp
def return_first_k_addresses(n,data):
    street_list={}
    top_k=data.head(n)
    i=0
    while i<n:
        # str_addr=top_k.iloc[i]["hospital_name"]+': '+top_k.iloc[i]["address"]+', '+top_k.iloc[i]["city"]+', '+top_k.iloc[i]["state"]+", "+str(int(top_k.iloc[i]["zip"]))
        street_list[top_k.iloc[i]["hospital_name"]] = top_k.iloc[i]["address"]+', '+top_k.iloc[i]["city"]+', '+top_k.iloc[i]["state"]+" "+str(int(top_k.iloc[i]["zip"]))
        i+=1
    return street_list