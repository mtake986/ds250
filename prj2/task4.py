#%% 
import pandas as pd
import altair as alt
import numpy as np
# %%

# %%
url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json"
flights = pd.read_json(url)
flights.head()
# %%
indexNames = flights[ flights['num_of_delays_late_aircraft'] == -999 ].index
indexNames
# %%
flights.drop(indexNames, inplace=True)
flights
# %%
flights_new = flights.assign(weather_late_aircraft = round(flights.num_of_delays_late_aircraft * .3, 0))[["airport_code", "month", "num_of_delays_late_aircraft", "num_of_delays_nas", "num_of_delays_weather", "num_of_delays_total", "weather_late_aircraft"]]
flights_new

# %%
for i in flights_new.month:
  if i in ['April', 'May', 'June', 'July', 'August']:
    flights_new = flights_new.assign(weather_delays_nas = round(flights.num_of_delays_nas * .4))
  else:
    flights_new = flights_new.assign(weather_delays_nas = round(flights.num_of_delays_nas * .65))
flights_new
# %%
eachAirport = flights_new.groupby('airport_code').sum()
eachAirport

#%%
eachAirport = (eachAirport
    .assign(
        total_weather_delays = (
            eachAirport.num_of_delays_weather
            + eachAirport.weather_late_aircraft
            + eachAirport.weather_delays_nas
        )
    )
)
eachAirport
#%%
eachAirport = (eachAirport
    .assign(
        proportion_of_weather_delayed_flights = round(
            eachAirport.total_weather_delays / eachAirport.num_of_delays_total * 100, 1
        )
    )
    .sort_values("proportion_of_weather_delayed_flights", ascending=False)
).reset_index()
eachAirport

# %%
chart = (
    alt.Chart(eachAirport)
        .mark_bar()
        .encode(
            x="proportion_of_weather_delayed_flights:Q",
            y="airport_code:N",
            color=alt.condition(
                alt.datum.proportion_of_weather_delayed_flights == eachAirport.proportion_of_weather_delayed_flights.max(),
                alt.value('orange'), # true
                alt.value('steelblue') # false
            )
        )
)
chart
# chart.save("./imgs/q4.png")
# %%

# %%
