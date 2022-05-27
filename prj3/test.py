
#%%
import pandas as pd
import sqlite3


#%% 
con = sqlite3.connect('lahmansbaseballdb.sqlite')

#%%
df = pd.read_sql_query("SELECT * FROM fielding", con)
df




# %%
len(df)
# %%
pd.read_sql_query("""
  select * 
  from batting 
  limit 5
""", con)

#%%
allTableInfo = pd.read_sql_query("""
  select * 
  from sqlite_master
  where type='table'
""", con)
allTableInfo
# %%
allTableNamesList = allTableInfo.tbl_name.unique()
allTableNamesList
# %%
for i in range(len(allTableNamesList)):
  print(allTableNamesList[i])
  
#%%
df2a = pd.read_sql_query("""
    SELECT playerid, yearid, teamid, stint
    FROM pitching
    WHERE playerid = 'anderla02'
""", con)
df2b = pd.read_sql_query("""
    SELECT *
    FROM salaries
    WHERE playerid = 'anderla02'
""", con)

# %%

pd.read_sql_query("""
  select p.playerid, p.yearid, p.teamid, stint, s.salary, (salary/1000)as salary_k
  from pitching AS p
    join salaries AS s on p.playerid = s.playerid
  where p.yearid > 1984 and p.playerid = 'anderla02'
  order by p.yearid
  limit 11
""", con)
# %%
df2c = pd.read_sql_query("""
    SELECT p.playerid, p.yearid, p.teamid, stint, salary, (salary/1000) AS salary_k
    FROM p
    JOIN salaries as s
        ON p.playerid = s.playerid
    WHERE p.yearid > 1984 AND p.playerid = 'anderla02'
    LIMIT 11
""", con)
df2c

#%%
# playerID, schoolID, salary, and the yearID/teamID associated with each salary. Order the table by salary (highest to lowest) and print out the table in your report.

#%%
byuCode = pd.read_sql_query("""
  SELECT * 
  FROM Schools
  WHERE schoolid LIKE '%byu%'
""", con)
# %%
q1 = pd.read_sql_query("""
  SELECT p.playerid, cp.yearid, salary
  FROM People AS p
    INNER JOIN Salaries AS s on p.playerid = s.playerid
    INNER JOIN CollegePlaying AS cp ON cp.playerid = p.playerid
  where p.playerid = 'catetr01' or p.playerid =  'lindsma01' or p.playerid = 'stephga01'
  GROUP BY cp.yearid
""", con)
q1
# %%
q1 = pd.read_sql_query("""
  SELECT cp.playerid, s.yearid, s.teamid, s.salary
  FROM CollegePlaying AS cp
    JOIN Salaries AS s on cp.playerid = s.playerid
  where cp.playerid = 'catetr01' or cp.playerid =  'lindsma01' or cp.playerid = 'stephga01'
  GROUP BY s.yearid
  ORDER BY s.salary DESC
""", con)
q1.to_markdown(index = False)
# %%
# %%
q1 = pd.read_sql_query("""
  SELECT cp.playerid, s.yearid, s.teamid, s.salary
  FROM CollegePlaying AS cp
    JOIN Salaries AS s on cp.playerid = s.playerid
  where cp.playerid = 'catetr01' or cp.playerid =  'lindsma01' or cp.playerid = 'stephga01'
  GROUP BY s.yearid
  ORDER BY s.salary DESC
""", con)
q1
# %%
