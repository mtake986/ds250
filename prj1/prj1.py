# %%
from turtle import color
import altair as alt
import pandas as pd
import numpy as np
#%%
url = "https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv"
names = pd.read_csv(url)


#%%
names.describe()

#### Grand 1 #####
# %%
myNameAtMyBirthYear = names.query("name == 'Jacob' & year == 2000 ")[["name", "year","Total"]]
myNameAtMyBirthYear
#%%
allMyName= names.query("name == 'Jacob'")[["name", "year","Total"]]
allMyName

#%%
print("Year: ", allMyName.query(f"Total == " + str(allMyName.Total.max())).year, "\nTotal: ", allMyName.query(f"Total == " + str(allMyName.Total.max())).Total)

#%%
chart = alt.Chart(allMyName).mark_bar().encode(
    x='year',
    y='Total',
    color=alt.condition(
        alt.datum.year == 2000,  # If the year is 1810 this test returns True,
        alt.value('orange'),     # which sets the bar orange.
        alt.value('steelblue')   # And if it's not true it sets the bar steelblue.
    )
)
chart
chart.save('charts/grand_q1_chart.png')



#### Grand 2 ####
# %%
brittany = names.query("name == 'Brittany'")[["name", "year","Total"]]
brittany
# %%
# min 
print("MINIMUM usage of Brittany")
min_brittany_year = brittany.query(f"Total == " + str(brittany.Total.min())).year
min_brittany_ttl = brittany.query(f"Total == " + str(brittany.Total.min())).Total
print(min_brittany_year, min_brittany_ttl)

# max
print("\nMAXIMUM usage of Brittany")
print("Year: ", brittany.query(f"Total == " + str(brittany.Total.max())).year, "\nTotal: ", brittany.query(f"Total == " + str(brittany.Total.max())).Total)

# so, the age of Brittany on the phone is about (2022 - 1990) = 32 while (2022 - 1968) = 54 is the most  unlikely. 

# %%
brit_chart = alt.Chart(brittany).mark_line().encode(
    x='year',
    y='Total',
)
brit_chart
# brit_chart.save('charts/grand_q2_chart.png')


#### Grand 3 #### 
#%%
chritianNames = names.query(
  "name == ['Mary', 'Martha', 'Peter', 'Paul'] & year >= 1920 & year <= 2000"
  )[["name", "year","Total"]]
chritianNames

#%%
mary = chritianNames.query("name == 'Mary'")[["name", "year","Total"]]
mary
#%%
mary_chart = (alt.Chart(mary)
    .mark_line(color="red")
    .encode(
        x = "year",
        y = "Total"
    )
)
mary_chart
#%%
martha = chritianNames.query("name == 'Martha'")[["name", "year","Total"]]
martha
martha_chart = (alt.Chart(martha)
    .mark_line(color="blue")
    .encode(
        x = "year",
        y = "Total"
    )
)
martha_chart
#%%
peter = chritianNames.query("name == 'Peter'")[["name", "year","Total"]]
peter
peter_chart = (alt.Chart(peter)
    .mark_line(color="orange")
    .encode(
        x = "year",
        y = "Total"
    )
)
peter_chart
#%%
paul = chritianNames.query("name == 'Paul'")[["name", "year","Total"]]
paul
paul_chart = (alt.Chart(paul)
    .mark_line(color="black")
    .encode(
        x = "year",
        y = "Total"
    )
)
paul_chart

#%%
allFour = mary_chart + martha_chart + peter_chart + paul_chart
allFour

#%%
all_chart = (alt.Chart(chritianNames)
    .mark_line()
    .encode(
        x = alt.X("year", axis=alt.Axis(title="Year")),
        y = alt.Y("Total", axis=alt.Axis(title="Total")),
        color = alt.Color("name", scale=alt.Scale(scheme='category10'))
    ).interactive()
)
all_chart
# all_chart.save('charts/grand_q3_chart.png')


#### Grand 4 ####
# %% 
anakin = names.query(
  "name == 'Anakin'")[["name", "year","Total"]]
anakin
#%%
anakin_chart = (alt.Chart(anakin)
    .mark_line()
    .encode(
        x = alt.X("year", axis=alt.Axis(title="Year")),
        y = alt.Y("Total", axis=alt.Axis(title="Total"))
    )
)

anakin_chart
anakin_chart.save('charts/grand_q4_chart.png')

#%%

leia = names.query(
  "name == 'Leia'")[["name", "year","Total"]]
leia
#%%
leia_chart = (alt.Chart(leia)
    .mark_line()
    .encode(
        x = alt.X("year", axis=alt.Axis(title="Year")),
        y = alt.Y("Total", axis=alt.Axis(title="Total"))
    )
)

leia_chart

#%%

rey = names.query(
  "name == 'Rey'")[["name", "year","Total"]]
rey
#%%
rey_chart = (alt.Chart(rey)
    .mark_line()
    .encode(
        x = alt.X("year", axis=alt.Axis(title="Year")),
        y = alt.Y("Total", axis=alt.Axis(title="Total"))
    )
)

rey_chart


#%%

bodhi = names.query(
  "name == 'Bodhi'")[["name", "year","Total"]]
bodhi
#%%
bodhi_chart = (alt.Chart(bodhi)
    .mark_line()
    .encode(
        x = alt.X("year", axis=alt.Axis(title="Year")),
        y = alt.Y("Total", axis=alt.Axis(title="Total"))
    )
)

bodhi_chart

#%%
sw = names.query(
  "name == ['Anakin', 'Leia', 'Rey', 'Bodhi']")[["name", "year","Total"]]
sw

#%%
starWarsChart = (alt.Chart(sw)
    .mark_line()
    .encode(
        x = alt.X("year", axis=alt.Axis(title="Year")),
        y = alt.Y("Total", axis=alt.Axis(title="Total")),
        color = alt.Color("name", scale=alt.Scale(scheme='category10'))
    ).interactive()
)
starWarsChart
starWarsChart.save('charts/star_wars_names_chart.png')


#%%
"""
url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
chartExample = (alt.Chart(mpg)
  .encode(
    x='displ', 
    y='hwy')
  .mark_circle()
)
chartExample
"""
#%%
text2 = (
alt.Chart
    ({'values':[{'x': 1968, 'y': 85}]})
.mark_text(text='1972')
.encode(x='x:Q', y='y:Q'))
text2

# %%
Oliver = names.query(
  "name == 'Oliver' & State == 'UT'")[["name", "year","Total"]].Total
sum(Oliver)
# %%
Felisha = names.query(
  "name == 'Felisha'")[["name", "year","Total"]]
Felisha
# %%
