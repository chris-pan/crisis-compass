from Update_Spreadsheet import filter_by_capacity, filter_by_state_calc_distance, access_data_by_name, return_first_k_addresses

ICU_PERCENTAGE = 0.75
INPATIENT_PERCENTAGE = 0.75
N = 10

# get user location
user_location = input()

hospital_data = pd.read_csv("https://healthdata.gov/sites/default/files/reported_hospital_capacity_admissions_facility_level_weekly_average_timeseries_20210110.csv") # get the file
# taking specific columns from data
bed_data = pd.concat([hospital_data["state"],hospital_data["hospital_name"],hospital_data["address"],hospital_data["city"],hospital_data["zip"],hospital_data["inpatient_beds_used_7_day_sum"],hospital_data["inpatient_beds_7_day_sum"],hospital_data["icu_beds_used_7_day_sum"],hospital_data["total_icu_beds_7_day_sum"]],axis=1,keys=["state","hospital_name","address","city","zip","inpatient_beds_used_7_day_sum","inpatient_beds_7_day_sum","icu_beds_used_7_day_sum","total_icu_beds_7_day_sum"])
# calculating the percentage of inpatient and icu beds being used
bed_data["percentage inpatient"] = np.where(((bed_data["inpatient_beds_7_day_sum"]<=0) & (bed_data["inpatient_beds_used_7_day_sum"]<0)),np.NaN,bed_data["inpatient_beds_used_7_day_sum"]/bed_data["inpatient_beds_7_day_sum"])
bed_data["percentage icu"] = np.where(((bed_data["total_icu_beds_7_day_sum"]<=0) & (bed_data["icu_beds_used_7_day_sum"]<0)),np.NaN,bed_data["icu_beds_used_7_day_sum"]/bed_data["total_icu_beds_7_day_sum"])
# column for the distance to be calculated by Google API
bed_data["distance"] = np.NaN

# first filter all states out, sort by distance, and return hospitals with capacity under limits
filtered_df = filter_by_state_calc_distance(user_location, ICU_PERCENTAGE, INPATIENT_PERCENTAGE, bed_data)#--------------------------------------------This line--first filter
# can access a hospital by a comma separated address
best_hospital = access_data_by_name("2070 CLINTON AVENUE, Alameda, 94501", filtered_df)
# return the addresses(hosp name: addr) of the N hospitals that are closest to you
closest_hospitals = return_first_k_addresses(N, filtered_df)#-----------------------------------------------------then gather-> with both you get the list of hospitals closest
for hospital in closest_hospitals:
    name = hospital["hospital_name"]
    address = hospital["address"]
    percent_inpatient = hospital["inpatient_beds_used_7_day_sum"] / hospital["inpatient_beds_7_day_sum"]
    percent_icu = hospital["icu_beds_used_7_day_sum"] / hospital["total_icu_beds_7_day_sum"])
    print(name, address, percent_inpatient, percent_icu)

# ask user to choose one and provide directions
selected = input()

directions = # link to Google Maps directions for selected hospital's address
print(directions)