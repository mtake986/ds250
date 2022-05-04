# %%
msg = "Hello World"
print(msg)

# %%
msg = "Hello again"
print(msg)

# %%
import sys
!{sys.executable} -m pip install altair_saver

# %% 
import altair as alt  
import pandas as pd   
url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)

# chart = alt.Chart(mpg).mark_point().encode(
#     x='displ', 
#     y='hwy'
# )

chart = (alt.Chart(mpg)
  .encode(
    x='displ', 
    y='hwy')
  .mark_circle()
)
chart
chart.save("w1Prj0Chart.png")

# %%
import altair as alt
alt.__version__
# %%
print(mpg
    .head(5)
    .filter(["manufacturer", "model","year", "hwy"])
    .to_markdown(index=False))

# %%
