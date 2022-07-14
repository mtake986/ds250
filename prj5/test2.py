# %%
import pandas as pd 
import altair as alt
import numpy as np

#%%
s = pd.Series(['1. Ant.  ', '2. Bee!\n', '3. Cat?\t', '4. Beat?\t', np.nan])
s
#%%
s.str.strip()

#%%

s.str.strip('123.!? \n\t')
#%%
s.str.strip('1234.!? \n\t')

# %%

s2 = pd.Series(['1-20', '21-50', '51-80', '81-100', np.nan])
s3 = pd.Series(
    [
        "this is a regular sentence",
        "https://docs.python.org/3/tutorial/index.html",
        np.nan
    ]
)
#%%
s2.str.split()
#%%
s3.str.split()
#%%
s2.str.split(pat="-")
# %%
two_columns = s2.str.split("-", expand = True).rename(
   columns = {0: 'minimum', 1: 'maximum'})
two_columns
#%%
two_columns.fillna("").agg("__".join, axis = 1)

two_columns.minimum.str.cat(two_columns.maximum, sep = "__")


# %%
