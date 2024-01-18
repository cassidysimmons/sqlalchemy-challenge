# sqlalchemy-challenge
# Background
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area.

# Resources folder
- Included in the resources folder is two csv files and one sqlite file. The two csv files were used as refrences to what is included in the sqlite file, given that we cannot view the sqlite file on its own.
The sqlite file was used in both the climate_starter and app.py activities; we were tasked with querying the database in order to retreive many different statistics and make calculations.

# Climate_starter.ipynb
Within this jupyter notebook file contains a 'preciptation analysis' and a 'station analysis'.
After setting up the necessary engine and session, I used the 'inspector' tool to see which table contained the information needed to complete the analysis. I then calculated the date one year (365 days) from the latest date in the dataset, using that date range I was able to create a graph with the precipation data. Next, to start off the station analysis I determined how many stations there are in the stations table and found the 'most popular' station (the station with the most rows). I then was able to calculate the minimum, maximum, and average temperature observations for the most popular station found previously. Finally, I was able to create a graph of the most popular stations temperature observations vs frequency of said tobs. Last but not least, I closed the session, severing the connection to the database.

# App.py
Within this python file contains all the nescessary code to create a 'hawaii stations' api. 
After setting up the engine and establishing the session, I begun with the 'homepage' route which includes a welcome message and all available routes within the api. 
Next, the 'stations' route lists all of the available stations within the dataset. 
Next, to create the 'temperature observations' route I had to calculate the date one year (365 days) from the latest date in the dataset and find the most popular station (similar to the method used in climate_starter), then from that I was able to retreive the 'tobs' from that date range and station. 
Finally, for the 'dynamic routes' the user has to enter in a specified start and/ or end date and return the minimum, maximum, and average temperature observations within the specified range. 
For the 'dynamic start' route I had to instead include the user input date as a parameter/ filter. After filtering the date to be greater than or equal to the user input date, I was able to calculate the min, max and average for the specified date range. 
Lastly, for the 'dynamic start/ end' route an end date must be input by the user as well; instead of filtering the date to be greater than or equal to the user input date, I filtered the date range to be inbetween the specified start and end dates. 
