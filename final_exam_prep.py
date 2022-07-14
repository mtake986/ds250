#%%
import pandas as pd 
import altair as alt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics

# %%
url_names = 'https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv'
#%%
dat_names = pd.read_csv(url_names)
dat_names.head(5)
# %%
john = dat_names.query("name == 'John'")
len(john)
#%%
john_ut_or = john[["name", "year", "UT", "OR"]]
print(john_ut_or)
len(john_ut_or)
# %%
john_ut_chart = alt.Chart(john_ut_or).mark_line(color="orange").encode(
    x="year",
    y="UT",
)
john_ut_chart
# %%
john_or_chart = alt.Chart(john_ut_or).mark_line(color="red").encode(
    x="year",
    y="OR",
)
john_or_chart
# %%
ut_or_chart = john_ut_chart + john_or_chart
# %%
ut_or_chart = ut_or_chart.encode(
  x=alt.X(axis=alt.Axis(title='Year name given', labelColor=alt.condition('datum.value == 1936 && datum.value == 1976 && datum.value == 1999', alt.value('red'), alt.value('black')))),
  y=alt.Y(axis=alt.Axis(title='Count of John'))
).properties(
    title={
      "text": ["The history of John for Utah (red) and Oregon (orange)"]
    },
    width=800,
    height=300
)
# %%
ut_or_chart
# %%
overlay = pd.DataFrame({'x': [1936, 1976,1999]})
vline = (
  alt.Chart(overlay)
  .mark_rule()
  .mark_text(
    text=["1936", "1976","1999"]
  )
  .encode(
    x=alt.X("x",
            scale=alt.Scale(
                domain=[
                    1900,2020
                ]
            )
    ))
)
vline


# %%
line1 = pd.DataFrame({'x': [1936]})
line1_chart = (
  alt.Chart(line1)
  .mark_rule()
  .encode(
    x=alt.X("x",
            scale=alt.Scale(
                domain=[
                    1900,2020
                ]
            )
    ))
)
line1_chart

text1_chart = (
  alt.Chart(line1)
  .mark_text(
    text=["1936"],
    align='left', 
    dx=5, 
    dy=-5
  )
  .encode(
    x=alt.X("x",
            scale=alt.Scale(
                domain=[
                    1900,2020
                ]
            )
    ))
)
text1_chart

line2 = pd.DataFrame({'x': [1976]})
line2_chart = (
  alt.Chart(line2)
  .mark_rule()
  .encode(
    x=alt.X("x",
            scale=alt.Scale(
                domain=[
                    1900,2020
                ]
            )
    ))
)
line2_chart

text2_chart = (
  alt.Chart(line2)
  .mark_text(
    text=["1976"],
    align='left', 
    dx=5, 
    dy=-5
  )
  .encode(
    x=alt.X("x",
            scale=alt.Scale(
                domain=[
                    1900,2020
                ]
            )
    ))
)
text2_chart


line3 = pd.DataFrame({'x': [1999]})
line3_chart = (
  alt.Chart(line3)
  .mark_rule()
  .encode(
    x=alt.X("x",
            scale=alt.Scale(
                domain=[
                    1900,2020
                ]
            )
    ))
)
line3_chart

text3_chart = (
  alt.Chart(line3)
  .mark_text(
    text=["1999"],
    align='left', 
    dx=5, 
    dy=-5
  )
  .encode(
    x=alt.X("x",
            scale=alt.Scale(
                domain=[
                    1900,2020
                ]
            )
    ))
)
text3_chart

# %%

with_line = alt.layer(
  ut_or_chart,
  line1_chart, 
  text1_chart,
  line2_chart, 
  text2_chart, 
  line3_chart, 
  text3_chart, 
)
with_line


# %% ============= Q2 ===============
# Our computations can’t be done with missing values. Take the following series and calculate the mean after replacing the missing values with the median.
mister = pd.Series([np.nan, 15, 22, 45, 31, np.nan, 85, 38, 129, 8000, 21, 2])

# replace np.nan with median
sorted = mister.sort_values()
median = (31 + 38)/2
sorted.replace(np.nan, median, inplace=True)
sorted

sum(sorted) / len(sorted)


# %% ======== Q3 ============
q3 = pd.read_csv("https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_ml/dwellings_ml.csv")


# %%
q3.columns
# %%
q3.stories.unique() # array([2, 1, 3, 4])
# %%
q3_1_2_stories = q3.query("stories == [1, 2]")
q3_1_2_stories
# %%
