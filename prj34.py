#%% 
import pandas as pd
import altair as alt
import numpy as np
# %%
url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json"
flights = pd.read_json(url)
flights.head()

#%%
# First, leave 30% of the value in each late-arriving aircraft 

# Second, 
# - April to August, leave 40% of nas category
# - Rest, leave 65% of nas category
# %%
flights
#%%
indexNames = flights[ flights['num_of_delays_late_aircraft'] == -999 ].index
indexNames
# %%
flights.drop(indexNames, inplace=True)
flights
#%%

flights_new = flights.assign(weather_late_aircraft = round(flights.num_of_delays_late_aircraft * .4, 2))[["month", "num_of_delays_late_aircraft", "num_of_delays_nas", "weather_late_aircraft"]]

# %%
indexNames = flights_new[ flights_new['month'] == "n/a" ].index
indexNames
# %%
flights_new.drop(indexNames, inplace=True)
flights_new
# %%
for i in range(len(flights_new)):
  print(flights_new.query("index == 1"))
# %%
