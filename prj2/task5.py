#%% 
import pandas as pd
import altair as alt
import numpy as np
import json as json
# %%
url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json"
flights = pd.read_json(url)
flights.head()

# %%
flights.isnull().sum()
#%%
flights.dropna(inplace=True)
# %%
flights_new = flights.replace(["", -999, "n/a", "1500+"], np.nan)
flights_new.isnull().sum()

#%%
print(flights_new)
json_data = flights_new.to_json(orient="records")
print(json_data)

# %%
flights_new.to_json("q5.json", orient="records")
# %%

