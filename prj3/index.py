#%%
import pandas as pd
import sqlite3
#%%
con = sqlite3.connect('lahmansbaseballdb.sqlite')

df = pd.read_sql_query("SELECT * FROM fielding LIMIT 5", con)
df
# %%
