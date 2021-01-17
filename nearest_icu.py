import requests, json

# Google Maps distance api key
api_key ='Your_api_key'

table = # import table data

 # get user location
user_location = input()

# remove full hospitals
# remove hospitals that are > x% full?
state_table = # filter table to only hospitals in state

# url variable store url  
url ='https://maps.googleapis.com/maps/api/distancematrix/json?'

k_closest = []

for hospital in state_table:
    if len(k_closest) > k:
        break

    name = # hospital name
    dest = # hospital address
    full = # percent full

    # Get method of requests module 
    # return response object 
    r = requests.get(url + 'origins = ' + user_location +
                    '&destinations = ' + dest +
                    '&key = ' + api_key) 
    dist = r.json()

    k_closest.append([name, address, dist, full])

# sort by distance
k_closest = sorted(k_closest, key=lambda x:x[2])

# print k_closest hospital names + locations + distace + % full
print(k_closest)

# ask user to choose one and provide directions
selected = input()

print(directions)