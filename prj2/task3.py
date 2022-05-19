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
flights.isna().sum()
#%%
indexNames = flights[ flights['num_of_delays_late_aircraft'] == -999 ].index
indexNames
# %%
flights.drop(indexNames, inplace=True)
flights
#%%
# indexNames = flights[ flights['month'] == "n/a" ].index
# indexNames
# # %%
# flights.drop(indexNames, inplace=True)
# flights

#%%

flights_new = flights.assign(weather_late_aircraft = round(flights.num_of_delays_late_aircraft * .3, 0))[["month", "num_of_delays_late_aircraft", "num_of_delays_nas", "num_of_delays_weather",  "weather_late_aircraft"]]
flights_new

# # %%
# flights_new.query("month == ['April', 'May', 'June', 'July', 'August']").assign(weather_delays_nas = round(flights.num_of_delays_nas * .4, 0))
# flights_new
# #%%
# flights_new.query("month != ['April', 'May', 'June', 'July', 'August']").assign(weather_delays_nas = round(flights.num_of_delays_nas * .65, 0), inplace=True)
# flights_new

# %%
for i in flights_new.month:
  if i in ['April', 'May', 'June', 'July', 'August']:
    flights_new = flights_new.assign(weather_delays_nas = round(flights.num_of_delays_nas * .4))
  else:
    flights_new = flights_new.assign(weather_delays_nas = round(flights.num_of_delays_nas * .65))
flights_new

# %%

TotalDelayedFlightsDueToWeather = (
  flights_new.num_of_delays_weather.sum()
  + flights_new.weather_late_aircraft.sum()
  + flights_new.weather_delays_nas.sum()
)
TotalDelayedFlightsDueToWeather
# %%
flights.year.unique()
# %%
