import urllib   #to get the spreadsheet
import datetime #to get the calendar date
import os
import requestsdef exists(path):
    r = requests.head(path)
    return r.status_code == requests.codes['ok']

#first define path of file
#define the location
location="\\something\\something"
#define the file name
file_title="data.csv"
path=location.join(file_title)
#download the current file
dls="https://healthdata.gov/sites/default/files/reported_hospital_capacity_admissions_facility_level_weekly_average_timeseries_20210110.csv"

urllib.request.urlretrieve(dls,path)#downloads the file and saves to path

current_date=datetime.date
next_week=current_date+datetime.timedelta(days=7)
string_date=next_week.isoformat
print(string_date.replace('-',''))
next_dls="https://healthdata.gov/sites/default/files/reported_hospital_capacity_admissions_facility_level_weekly_average_timeseries_"+string_date+".csv" #next file to download

while(True):#has to run forever to check if the file exists
    #constantly update the time
    #if file exists- a week has passed already
    if(exists(next_dls)):
        #first delete current file
        os.remove(path)
        #download new file
        urllib.request.urlretrieve(next_dls,path)
        #update the next_dls link
        current_date=next_week
        next_week=current_date+datetime.timedelta(days=7)
        string_date=next_week.isoformat
        print(string_date.replace('-',''))
        next_dls="https://healthdata.gov/sites/default/files/reported_hospital_capacity_admissions_facility_level_weekly_average_timeseries_"+string_date+".csv"


    

