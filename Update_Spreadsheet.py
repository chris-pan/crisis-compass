import pandas as pd
import datetime
import numpy as np


## just kept a separate filtering method though it could be kept in the same line, change if want
def filter_by_capacity(icu_percentage, inpatient_percentage, data):
    return data[((data["percentage inpatient"]<inpatient_percentage) & (data["percentage inpatient"]>=0.0))|((data["percentage icu"]<icu_percentage) & (data["percentage icu"]>=0.0))]

#first filters by state, calculates and sorts the df by distance, then if you want, can filter by threshold icu inpatient
def filter_by_state_calc_distance(current_location, icu_percentage, inpatient_percentage, data):
    #assuming that will get an address
    my_state=current_location[-2:]#grabbing the state from the last two letters of the address- make sure no trailing spaces in str
    state_df=data.query('state==@my_state') # can add filter for percentage in icu or inpatient
    ##################################PUT UR GOOGLE DISTANCE STUFF HERE
    #for row in len(state_df):
    #    state_df["distance"][row]=distance(current_location,state_df['address'][row])
    #state_df.sort_values(by=["distance"])--sort dataframe by distance in ascending order-> can pick the k closest by then
    return filter_by_capacity(icu_percentage,inpatient_percentage,state_df)
    
    #search by address STREET NAME, CITY, ZIP CODE
    #will only search by street name and zip code since the matching
    #for the city sucks
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
    street_list=[]
    top_k=data.head(n)
    i=0
    while i<n:
        str_addr=top_k.iloc[i]["hospital_name"]+': '+top_k.iloc[i]["address"]+', '+top_k.iloc[i]["city"]+', '+top_k.iloc[i]["state"]+", "+str(int(top_k.iloc[i]["zip"]))
        street_list.append(str_addr)
        i+=1
    return street_list


hospital_data=pd.read_csv("https://healthdata.gov/sites/default/files/reported_hospital_capacity_admissions_facility_level_weekly_average_timeseries_20210110.csv") # get the file
#taking specific columns from data
bed_data=pd.concat([hospital_data["state"],hospital_data["hospital_name"],hospital_data["address"],hospital_data["city"],hospital_data["zip"],hospital_data["inpatient_beds_used_7_day_sum"],hospital_data["inpatient_beds_7_day_sum"],hospital_data["icu_beds_used_7_day_sum"],hospital_data["total_icu_beds_7_day_sum"]],axis=1,keys=["state","hospital_name","address","city","zip","inpatient_beds_used_7_day_sum","inpatient_beds_7_day_sum","icu_beds_used_7_day_sum","total_icu_beds_7_day_sum"])
#calculating the percentage of inpatient and icu beds being used
bed_data["percentage inpatient"]=np.where(((bed_data["inpatient_beds_7_day_sum"]<=0) & (bed_data["inpatient_beds_used_7_day_sum"]<0)),np.NaN,bed_data["inpatient_beds_used_7_day_sum"]/bed_data["inpatient_beds_7_day_sum"])
bed_data["percentage icu"]=np.where(((bed_data["total_icu_beds_7_day_sum"]<=0) & (bed_data["icu_beds_used_7_day_sum"]<0)),np.NaN,bed_data["icu_beds_used_7_day_sum"]/bed_data["total_icu_beds_7_day_sum"])
#column for the distance to be calculated by Google API
bed_data["distance"]=np.NaN

#first filter all states out, sort by distance, and return hospitals with capacity under limits
filtered_df=filter_by_state_calc_distance("CA",0.50,0.50,bed_data)#--------------------------------------------This line--first filter
#can access a hospital by a comma separated address
best_hospital=access_data_by_name("2070 CLINTON AVENUE, Alameda, 94501",
filtered_df)
#return the addresses(hosp name: addr) of the k hospitals that are closest to you
closest_hospitals=return_first_k_addresses(10,filtered_df)#-----------------------------------------------------then gather-> with both you get the list of hospitals closest
#just prints the addr
for addr in closest_hospitals:
    print(addr)
