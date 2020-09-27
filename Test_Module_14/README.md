# Bike-Sharing

## Overview
Last summer, my friend Kate and I took the trip of a lifetime. New York City for two full weeks exploring historic landmarks like Central Park, the Statue of Liberty, and the Empire State Building. It was a magical experience and as we flew home together we looked through our vacation photos and had a realization. One of the key ingredients to the magic was an unlikely suspect, ***CitiBike***. Kate and I had biked everywhere which allowed us to really get to know the city and interact with the people who lived there and who were using bikes for their commutes. Back home, we thought what if we could start a similar bike share business for our hometown of Des Moines, Iowa. Kate and I start brainstorming and a few weeks later she called me with some incredible news. She has a potential angel investor who might be interested in providing seed funding to explore a bike-share program in Des Moines. This is an exciting prospect but you know you have to think realistically. The mechanics of making this business work might be quite different in Des Moines than in NYC. You decide that the first step is to figure out how the bike-share business actually works in NYC. From there you will create a proposal on how it might work in Des Moines. Kate is gregarious, friendly, and fearless. She should definitely be the face of the proposal. However, I have the data analytics experience and will take the lead on figuring out how this project might actually work.

## Purpose
In the past Kate and I used Tableau to create some basic visualization and created a short Tableau story.

Now that we've gotten a good idea of how to create our story, there is still some more work to be done to convince investors that a bike-sharing program in Des Moines is a solid business proposal. We decided that we will create some more visualizations and then add these new visualizations to the two we created in the past for our final presentation and analysis to pitch to investors.

## Resources
* Software: Visual Studio Code 1.49.1, Tableau Desktop (Public Version - 2020.3.0), Anaconda
* Language(s): Python for ETL
* Other Tool(s): Tableau for Visualization
* Data Source(s): 
    * Raw Data - https://s3.amazonaws.com/tripdata/201908-citibike-tripdata.csv.zip

## Results

[***Link to Dashboard***](https://public.tableau.com/profile/govind6013#!/vizhome/Des_Moines_Bikesharing_Business_Proposal/Business_Proposal)

1. ### Some basic information gathered from the data 

    **Image 1 (below)**

    ![](Images/Basic_info.png)

    **Observation/Description:**
    * The total number of rides in NYC in the month of August 2019 was 2,344,224. While this data relates to NYC, it can use used to get a rough estimate of the ridership in a city, for example the population of Des Moines is 216,853.
    * 81.07% of all rides were taken by Subscribers, while 18.93% was taken by Customers
    * Males took 65.28% of the rides, Females 25.1% and Unknowns at 9.62%

2. ### Top Starting and Ending locations
    **Image 2 (below)**

    ![](Images/Top_starting_and_ending_locations.png)

    **Observation/Description:**
    * Downtown Manhattan was the top starting and ending location
    * This can be attributed to the fact that it has highest density of offices (thus commuters) as well as tourist spots (thus tourists)

3. ### Busiest times in a day

    **Image 3 (below)**
    ![](Images/peak_hours_of_day.png)

    **Observation/Description:**
    * In the morning, the number of rides start picking up between 7-8 AM, peaking between 8-9 AM, and then slowing between 10-11 AM.
    * In the evening, the number of rides start picking between 4-5 AM, peaking between 5-6 PM and slowing between 8-9 AM. 
    * The above both trends can be attributed to office commuters.
    * This also tells us that the morning times can be used to repair bikes

4. ### Tripduration

    **Image 4 (below)**
    ![](Images/tripduration.png)

    **Observation/Description:**
    * The number of trips with duration increases as we move from 1 hour to 5 hours, 5-6 hours is the peak
    * As the duration increases the number of trips start decreasing, although the decrease is slower as compared to the rise in the point above.


5. ### Tripduration by Gender

    **Image 5 (below)**
    ![](Images/tripduration_by_gender.png)

    **Observation/Description:**
    * for Males, the number of trips with duration increases as we move from 1 hour to 5 hours, 5-6 hours is the peak
    * for Males, as the duration increases the number of trips start decreasing, although the decrease is slower as compared to the rise in the point above.
    * For Females and Unknown, the trend is similar

6. ### Trips by Weekday per hour
    **Image 6 (below)**
    ![](Images/CountofTrips_by_weekdays.png)
    **Observation/Description:**
    * This matches our analysis of peak hours in a day (point 3)
    * In the morning, the peak hours are betwen 7-10 AM and post noon, the peak hours are 5-8 PM, presumably becaused of office commuters.
    * Weekdays were usually busier than weekends
    * Thursday as the busiest day
    * Wednesday was a unusually less-busy day.
    * Bike service should be scheduled in the mornings, or on Wednesday afternoons, as Thursdays are very busy

7. ### Trips by Gender (Weekday per Hour)
    **Image 7 (below)**
    ![](Images/CountofTrips_by_weekdays_by_gender.png)

    **Observation/Description:**
    * The results are a mirror of what we found in the step above
    * As Males constitute 65.28% of the riders, the male data is more pronounced as compared to other genders

8. ### Trips by Gender and User-type

    **Image 8 (below)**
    ![](Images/CountOfTrips_by_UserType_and_gender.png)

    **Observation/Description:**
    * With 81% of users as Subscribers, 65.28% as Males, and Weekdays busier than Weekends, and Thursday as the busiest day, it comes as no surprise as the field with the most trips was corresponding to Male Subscribers on Thursday, follwed by Friday, Tuesday, Monday, Saturday, Wednesday and Sunday.
    * The least busy day of the Male Subscribers is busier than the busiest days of the other groups.

## Summary

August is usually a good time to visit NYC, which means the data has the best ridership of any month of the year. Winters will see less ridership.

Des Moines is very small as compared to NYC, in terms of pouplation and area. 
It is suggested that we have some 


2 additional suggestions for future analysis
1. We already have a visualization for number of trip by Gender, user-type, weekdays. We can dig deeper to find the breakdown on the hours of weekdays.


=============




Analysis (24 points)
The written analysis has the following:

Overview of the statistical analysis:

The purpose of the analysis is well defined. (5 pt)
Results:

There are at least seven visualizations for the NYC Citibike analysis (7 pt)
There is a description of the results for each visualization (7 pt)


Summary:

There is a high-level summary of the results and two additional visualizations are suggested for future analysis (5 pt)

1.

## Business Proposal to the stakeholders

[<img src="Images/DesMoinesBikeShareProposal.png">](https://public.tableau.com/profile/govind6013#!/vizhome/Des_Moines_Bikesharing_Business_Proposal/Business_Proposal)


