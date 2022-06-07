

# Set up 
```python
# import modules
import pandas as pd
import altair as alt
import numpy as np
# import data through url
url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json"
flights = pd.read_json(url)
flights.head()
```

# Project 1 
### Simple chart
``` python 
alt.Chart(ttl).mark_bar().encode(
    y="airport_code",
    x="num_of_flights_total",
)
```

### How to create a dataframe by myself
``` python
data = {'airport_code':['ATL', 'DEN', 'IAD', 'ORD', 'SAN', 'SFO', 'SLC'],
        'PropOfDelay':[atlPropOfDelay, denPropOfDelay, iadPropOfDelay, ordPropOfDelay, sanPropOfDelay, sfoPropOfDelay, slcPropOfDelay]}

# Create DataFrame
df = pd.DataFrame(data)
```

### Chart: change a color conditionally
``` python
chart_num_of_flights_total = (
    alt.Chart(group)
        .mark_bar()
        .encode(
            x="num_of_flights_total",
            y="airport_code",
            color=alt.condition(
                alt.datum.num_of_flights_total == group.num_of_flights_total.max(),
                alt.value('orange'), # true
                alt.value('steelblue') # false
            )
        )
)
```

### Store the chart in a png version
``` python
chart_name.save("./imgs/whatever.png")
```

### Table data to markdown 
``` python
print(df.to_markdown(index = False))
```

### Rename a column name 
``` python
# %%
df.rename(columns = {'old': 'new'}, inplace=True)
```



# Project 2

### na
``` python
# no duplicated values
flights.month.unique()
# num of pandas na in a dataframe
flights.isna().sum()
# drop na from a dataframe
flights.dropna()
# Make a list storing indexes whose one of the rows have a specfic value
indexNames = flights[flights['num_of_delays_late_aircraft'] == -999 ].index
# Then, drop the rows
flights.drop(indexNames, inplace=True)
```

#### replace() 
```python
(flights_copy
    .query("airport_code == 'IAD' & year==2006")
    .replace("n/a", "September", inplace=True))
```
### assign()
``` python
flights_new = (flights
    .assign(
        weather_late_aircraft = round(
            flights.num_of_delays_late_aircraft * .3, 0))
            [[
                "num_of_delays_late_aircraft", 
                "num_of_delays_nas", 
                "num_of_delays_weather",  
                "weather_late_aircraft"
            ]]
)
```
### chart: range 
```python
alt.Chart(ttl).mark_point().encode(
    x=alt.X("year:Q", 
            scale=alt.Scale(
                domain=[
                    flights.year.min() - 1, 
                    flights.year.max() + 1
                ]
            )
    ),
    y=alt.Y("num_of_flights_total:Q"),
            color = alt.Color("airport_code:N", scale=alt.Scale(scheme='category10')
    ),
    shape='airport_code:N',
).interactive()
```

# Project 3
## Import sql file
```python
con = sqlite3.connect('lahmansbaseballdb.sqlite')
```



