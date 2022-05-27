
#%%
import pandas as pd
import sqlite3


#%% 
con = sqlite3.connect('lahmansbaseballdb.sqlite')

# %%
q1 = pd.read_sql_query("""
  SELECT cp.playerid, cp.schoolid, s.yearid, s.teamid, (s.salary/1000) AS k_salary
  FROM CollegePlaying AS cp
    JOIN Salaries AS s on cp.playerid = s.playerid
  where cp.playerid = 'catetr01' or cp.playerid =  'lindsma01' or cp.playerid = 'stephga01'
  GROUP BY s.yearid
  ORDER BY s.salary DESC
""", con)
q1
# %%
q1.to_markdown(index = False)
# %%
