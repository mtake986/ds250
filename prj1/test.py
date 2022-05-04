# Load libraries

#%%
import altair as alt
import pandas as pd
import numpy as np

#%%
# Read in data.  I've saved the file to my working folder to save time loading

#url = "https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv"
url = "https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv"
names = pd.read_csv(url)

#%%

#### Setting up a subset of data for a specific name
charles = names.query("name == 'Charles'")[["name", "year", "Total"]]

#%%
# Or equivalently using .filter()
charles = names.query("name == 'Charles'").filter(items=["name", "year", "Total"])

charles
#%%
# I can make this even more readable by using parentheses
# This doesn't look like much now, but makes it much easier to read when you have lots of methods chained
charles = (names
	.query("name == 'Charles'")
	.filter(items=["name", "year", "Total"])
)

##Creating the main chart
#%%
chart = (alt.Chart(charles)
    .mark_line()
    .encode(
        x = "year",
        y = "Total"
    )
)
chart

#%%
c49 = charles.query("year == 1949")
c49

#%%

new_chart = (alt.Chart(c49, title="Popularity of Charles")
    .mark_circle(color="red", size=100)
    .encode(
        x = alt.X("year"),
        y = alt.Y("Total")
    ).interactive()
)

new_chart

#%%

### I can create a final chart by adding the two together.
### Order matters. The second chart will be aligned to the dimensions of the first

final_chart = chart + new_chart
final_chart

### Save the chart

#%%
final_chart.save("charles_1949.png")


########## Practice #############
#%%
k = (names
	.query("name == 'Kelly'")
	.filter(items=["name", "year", "Total"])
)
k

#%%
j = (names
	.query("name == 'Jacob'")
	.filter(items=["name", "year", "Total"])
)
j
#%%
k_chart = (alt.Chart(k)
    .mark_line()
    .encode(
        x = "year",
        y = "Total"
    )
)
k_chart
# %%
j_chart = (alt.Chart(j)
    .mark_line(color="red")
    .encode(
        x = "year",
        y = "Total"
    )
)
j_chart

# %%
kj_chart = k_chart + j_chart
kj_chart

# %%

# %%
