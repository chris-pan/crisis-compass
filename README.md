# crisis-compass
HackDavis 2021
### Navigate to a safer direction

## Inspiration
Our inspiration was from the news of how the ICUs were reaching full capacity for taking in Covid Patients. Though we have not addressed the current issue of nurses being overworked by including the current number of beds being staffed, I believe that we can help guide newly infected Covid patients to ICU clinics that can accept more patients in order to offload the stress crowded ICUs are facing.
Due to current circumstances surrounding the pandemic, hospitals have been overwhelmed with COVID-19 patients, most being near full capacity. To avoid patients in need of urgent care being turned away, our team has come up with a mobile solution: Crisis Compass.
## What it does
Crisis Compass locates ICUs that have capacity and are closest to the user's location and provides them with directions.
## How we built it
We pulled the ICU data which is updated weekly from healthcare.gov to use for Crisis Compass. After obtaining user location, the application filters data based on distance from the user calculated with Google's Distance Matrix API and how full the ICU is calculated from the ICU data. 
## Challenges we ran into
We had to understand how to accurately read the healthcare.gov dataset and select the information necessary to allow our application to provide the user with the correct ICUs. In addition we had to account for all sorts of user input possibilities as querying the Distance Matrix API and creating a Google Maps link required specific formats for the links.
## Accomplishments that we're proud of
We're proud of getting the backend functionality of the application running and of creating a concept for what the app would actually look like for users.
## What we learned
We learned how to parse online datasets with the pandas package from python . We also learned how to develop design prototypes using Figma, where we worked on branding through color schemes, font design, and logo/slogan.
## What's next for Crisis Compass
Although we have the backend functionality and a concept for the frontend done, we haven’t created the actual application yet. Our next steps would be to bring our idea to life and create the mobile application, using tools such as Flutter. 
