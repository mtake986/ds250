#%% 
import pandas as pd
import altair as alt
import numpy as np
# %%
url = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json"
flights = pd.read_json(url)
flights.head()

#%%
airports = flights.airport_code.unique()
airports

# %%
atl = flights.query("airport_code == 'ATL'")
den = flights.query("airport_code == 'DEN'")
iad = flights.query("airport_code == 'IAD'")
ord = flights.query("airport_code == 'ORD'")
san = flights.query("airport_code == 'SAN'")
sfo = flights.query("airport_code == 'SFO'")
slc = flights.query("airport_code == 'SLC'")

# %%
flights.columns

# %%
group = flights.groupby("airport_code").sum()[["num_of_flights_total", "num_of_delays_total", "minutes_delayed_total"]]
group
# %%
atlFlightTtl = atl.sum()[["num_of_flights_total"]]
atlDelayTtl = atl.sum()[["num_of_delays_total"]]
atlMinDelayTtl = atl.sum()[["minutes_delayed_total"]]
atlPropOfDelay = int(atlDelayTtl) / int(atlFlightTtl) * 100
atlAvgMinDelayed = int(atlMinDelayTtl) / int(atlFlightTtl)

# %%
denFlightTtl = den.sum()[["num_of_flights_total"]]
denDelayTtl = den.sum()[["num_of_delays_total"]]
denMinDelayTtl = den.sum()[["minutes_delayed_total"]]
denPropOfDelay = int(denDelayTtl) / int(denFlightTtl) * 100
denAvgMinDelayed = int(denMinDelayTtl) / int(denFlightTtl)

# %%
iadFlightTtl = atl.sum()[["num_of_flights_total"]]
iadDelayTtl = atl.sum()[["num_of_delays_total"]]
iadMinDelayTtl = atl.sum()[["minutes_delayed_total"]]
iadPropOfDelay = int(iadDelayTtl) / int(iadFlightTtl) * 100
iadAvgMinDelayed = int(iadMinDelayTtl) / int(iadFlightTtl)

# %%
ordFlightTtl = ord.sum()[["num_of_flights_total"]]
ordDelayTtl = ord.sum()[["num_of_delays_total"]]
ordMinDelayTtl = ord.sum()[["minutes_delayed_total"]]
ordPropOfDelay = int(ordDelayTtl) / int(ordFlightTtl) * 100
ordAvgMinDelayed = int(ordMinDelayTtl) / int(ordFlightTtl)
# %%
sanFlightTtl = san.sum()[["num_of_flights_total"]]
sanDelayTtl = san.sum()[["num_of_delays_total"]]
sanMinDelayTtl = san.sum()[["minutes_delayed_total"]]
sanPropOfDelay = int(sanDelayTtl) / int(sanFlightTtl) * 100
sanAvgMinDelayed = int(sanMinDelayTtl) / int(sanFlightTtl)
# %%
sfoFlightTtl = sfo.sum()[["num_of_flights_total"]]
sfoDelayTtl = sfo.sum()[["num_of_delays_total"]]
sfoMinDelayTtl = sfo.sum()[["minutes_delayed_total"]]
sfoPropOfDelay = int(sfoDelayTtl) / int(sfoFlightTtl) * 100
sfoAvgMinDelayed = int(sfoMinDelayTtl) / int(sfoFlightTtl)
# %%
slcFlightTtl = slc.sum()[["num_of_flights_total"]]
slcDelayTtl = slc.sum()[["num_of_delays_total"]]
slcMinDelayTtl = slc.sum()[["minutes_delayed_total"]]
slcPropOfDelay = int(slcDelayTtl) / int(slcFlightTtl) * 100
slcAvgMinDelayed = int(slcMinDelayTtl) / int(slcFlightTtl)
round(slcPropOfDelay, 1)

# %%
flights.isna().sum()

# %%
flights.head()

# %%
avg = np.round(flights.groupby('airport_code').agg(avg_minDelayedTtl = ('minutes_delayed_total', np.average))).reset_index()
avg

# %%
alt.Chart(avg).mark_line().encode(
    y='airport_code:N',
    x='minutes_delayed_total:Q',
)

# %%
group
# %%
flights.query("month == 'n/a'")
# %%
iad.query("year == 2006").month.replace("n/a", "September", inplace=True)

# %%
flights_copy = flights.copy()
# %%
flights_copy.query("airport_code == 'IAD' & year==2006").replace("n/a", "September", inplace=True)
# %%
drpFli = flights.dropna()
# %%
drpFli.isna().sum()
# %%
drpFli.month.unique()
# %%
indexNames = drpFli[ drpFli['month'] == "n/a" ].index
indexNames
# %%
drpFli.drop(indexNames, inplace=True)

# %%
drpFli.month.unique()
# %%
flights.query("index == 1")["month"]

# %%
len(drpFli)

#%%

ttl = flights.groupby('airport_code').sum().reset_index()
ttl
#%%
monthPropOfDelay = flights.groupby('month').sum().reset_index()
monthPropOfDelay
#%%
alt.Chart(monthPropOfDelay).mark_bar().encode(
    y="month",
    x="num_of_delays_total",
)
#%%
alt.Chart(ttl).mark_point().encode(
    x=alt.Y("year:Q", scale=alt.Scale(domain=[flights.year.min() - 1, flights.year.max() + 1])),
    y=alt.Y("num_of_flights_total:Q"),
    color = alt.Color("airport_code:N", scale=alt.Scale(scheme='category10')),
    shape='airport_code:N',
).interactive()

#%%
flights.groupby("airport_code")['num_of_flights_total'].mean()
# %%
ttl = flights.groupby('airport_code')['num_of_flights_total'].sum().reset_index()

#%%
alt.Chart(ttl).mark_bar().encode(
    y="airport_code",
    x="num_of_flights_total",
)

#%%
flights["airport_code"]
#%%
data = {'airport_code':['ATL', 'DEN', 'IAD', 'ORD', 'SAN', 'SFO', 'SLC'],
        'PropOfDelay':[atlPropOfDelay, denPropOfDelay, iadPropOfDelay, ordPropOfDelay, sanPropOfDelay, sfoPropOfDelay, slcPropOfDelay]}

# Create DataFrame
dfPropOfDelay = pd.DataFrame(data)

# Print the output.
dfPropOfDelay

#%%
df = drpFli.groupby('month')['num_of_delays_total'].sum().reset_index()
df
#%%
alt.Chart(dfPropOfDelay).mark_bar().encode(
    x="PropOfDelay",
    y="airport_code",
)

# %%
group
# %%

list(round(group["minutes_delayed_total"] / 60))
list(group["minutes_delayed_total"])
# %%
group['minutes_delayed_total'] = group["minutes_delayed_total"].replace(list(group["minutes_delayed_total"]), list(round(group["minutes_delayed_total"] / 60)))

#%%
group.rename(columns = {'minutes_delayed_total':'delayed_total_in_hours'}, inplace = True)
group
# %%
group
# %%
group['delayed_total_in_hours'] = group["delayed_total_in_hours"].replace(list(group["delayed_total_in_hours"]), list(round(group["delayed_total_in_hours"] / group["num_of_flights_total"], 3)))

# %%
group

#%%
dfPropOfDelay
list(round(dfPropOfDelay.PropOfDelay, 2))

# %%
group.assign(proportion_of_delayed_flights = dfPropOfDelay["PropOfDelay"], inplace=True)
group

# %%
group["proportion_of_delayed_flights"] = list(round(dfPropOfDelay.PropOfDelay, 2))
group.reset_index(inplace=True)

# %%
chart_proportion_of_delayed_flights = alt.Chart(group).mark_bar().encode(
    x="proportion_of_delayed_flights",
    y="airport_code",
    color=alt.condition(
        alt.datum.proportion_of_delayed_flights == group.proportion_of_delayed_flights.max(),
        alt.value('orange'),
        alt.value('steelblue')
    )
)
chart_proportion_of_delayed_flights
# %%
chart_num_of_flights_total = alt.Chart(group).mark_bar().encode(
    x="num_of_flights_total",
    y="airport_code",
    color=alt.condition(
        alt.datum.num_of_flights_total == group.num_of_flights_total.max(),
        alt.value('orange'),
        alt.value('steelblue')
    )
)
chart_num_of_flights_total
# %%
chart_num_of_delays_total = alt.Chart(group).mark_bar().encode(
    x="num_of_delays_total",
    y="airport_code",
    color=alt.condition(
        alt.datum.num_of_delays_total == group.num_of_delays_total.max(),
        alt.value('orange'),
        alt.value('steelblue')
    )
)
chart_num_of_delays_total
# %%
chart_delayed_total_in_hours = alt.Chart(group).mark_bar().encode(
    x="delayed_total_in_hours",
    y="airport_code",
    color=alt.condition(
        alt.datum.delayed_total_in_hours == group.delayed_total_in_hours.max(),
        alt.value('orange'),
        alt.value('steelblue')
    )
)
# %%
all_chart = chart_num_of_flights_total | chart_num_of_delays_total | chart_proportion_of_delayed_flights | chart_delayed_total_in_hours 
all_chart.save("./imgs/q1.png")
# %%
print(group.to_markdown(index = False))
# %%
group.rename(columns = {'delayed_total_in_hours': 'average_delayed_hour'}, inplace=True)
group
# %%

######### Q2

flights.dropna(inplace=True)
# %%
flights.isna().sum()
# %%
indexNames = flights[ flights['month'] == "n/a" ].index
indexNames
# %%
flights.drop(indexNames, inplace=True)
flights

# flights.groupby('month').sum().reset_index()
# %%
monthFlight = flights.groupby('month')["month", "num_of_flights_total", "num_of_delays_total", "minutes_delayed_total"].sum().reset_index()
monthFlight


#%%
# list(round(monthFlight.num_of_delays_total / monthFlight.num_of_flights_total, 2))

monthFlight = monthFlight.assign(proportion_of_delayed_flights = round(monthFlight.num_of_delays_total / monthFlight.num_of_flights_total, 2))

#%%

monthFlight = monthFlight.assign(average_minutes_delayed = round(monthFlight.minutes_delayed_total / monthFlight.num_of_flights_total, 2))

monthFlight

#%%
print(monthFlight.to_markdown())


# %%
month_num_of_flights_total = alt.Chart(monthFlight).mark_bar().encode(
    x="num_of_flights_total",
    y="month",
    color=alt.condition(
        alt.datum.num_of_flights_total == monthFlight.num_of_flights_total.max(),
        alt.value('orange'),
        alt.value('steelblue')
    )
)
month_num_of_flights_total
# %%
month_num_of_delays_total = alt.Chart(monthFlight).mark_bar().encode(
    x="num_of_delays_total",
    y="month",
    color=alt.condition(
        alt.datum.num_of_delays_total == monthFlight.num_of_delays_total.max(),
        alt.value('orange'),
        alt.value('steelblue')
    )
)
month_num_of_delays_total
# %%
month_hours_delayed_total = alt.Chart(monthFlight).mark_bar().encode(
    x="hours_delayed_total",
    y="month",
    color=alt.condition(
        alt.datum.hours_delayed_total == monthFlight.hours_delayed_total.max(),
        alt.value('orange'),
        alt.value('steelblue')
    )
)
month_hours_delayed_total
# %%
month_proportion_of_delayed_flights = alt.Chart(monthFlight).mark_bar().encode(
    x="proportion_of_delayed_flights",
    y="month",
    color=alt.condition(
        alt.datum.proportion_of_delayed_flights == monthFlight.proportion_of_delayed_flights.max(),
        alt.value('orange'),
        alt.value('steelblue')
    )
)
month_proportion_of_delayed_flights
# %%
month_average_minutes_delayed = alt.Chart(monthFlight).mark_bar().encode(
    x="average_minutes_delayed",
    y="month",
    color=alt.condition(
        alt.datum.average_minutes_delayed == monthFlight.average_minutes_delayed.max(),
        alt.value('orange'),
        alt.value('steelblue')
    )
)
month_average_minutes_delayed
#%%
monthChart = month_num_of_flights_total | month_num_of_delays_total | month_hours_delayed_total | month_proportion_of_delayed_flights | month_average_minutes_delayed

monthChart
#%%
monthChart.save("./imgs/q2.png")

# %%
