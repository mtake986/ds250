
#%%
import pandas as pd
import sqlite3
import altair as alt


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

###############
### Task 2a ###
###############

#%%
q2a = pd.read_sql_query("""
  select playerID, yearID, AB, H, H*1000 / AB AS Average_Hits
  from Batting
  where AB >= 1
  order by Average_Hits desc, playerID 
  limit 5
""", con)
q2a.to_markdown(index = False)

# %%
q2b = pd.read_sql_query("""
  select playerID, yearID, AB, H, (H * 1000 / AB) AS Average_Hits
  from Batting
  where AB >= 10
  order by Average_Hits desc, playerID 
  limit 5
""", con)
q2b.to_markdown(index = False)
# %%
q2c = pd.read_sql_query("""
  select playerID, yearID, SUM(AB) AS Carrer_At_Bats, SUM(H) AS Career_Hits, SUM(H)*1000 / SUM(AB) AS Average_Hits
  from Batting
  group by playerID
  having Carrer_At_Bats >= 100
  order by Average_Hits desc, playerID 
  limit 5
""", con)
q2c.to_markdown(index = False)
# round(cast(H as float) / cast(AV as float), 3) as 'Batting_Average'

###############
### Task 3 ###
###############


# %%
q3a = pd.read_sql_query("""
  select name, yearID, AB, H, round(cast(H as float) / cast(AB as float), 3) as 'Batting_Average'
  from Teams
  where (lgID = 'NL' or lgID = 'AL') and name = 'Boston Red Sox' or name='Chicago White Sox'
""", con)
q3a
# %%
batting_average = alt.Chart(q3a).mark_line().encode(
    x=alt.X("yearID",
        scale=alt.Scale(
            domain=[
                1910, 
                2020,
            ]
        )
    ),
    y=alt.Y("Batting_Average"),
            color = alt.Color("name", scale=alt.Scale(scheme='category10')
    ),
).interactive()
batting_average
# %%
was_salary = pd.read_sql_query("""
  select teamID, sum(salary) as sum_salary, yearID
  from Salaries
  where teamID = 'WAS'
  group by yearID
""", con)
was_salary

# %%
atl_salary = pd.read_sql_query("""
  select teamID, sum(salary) as sum_salary, yearID
  from Salaries
  where teamID = 'ATL'
  group by yearID
""", con)
atl_salary

# %%
was = alt.Chart(was_salary).mark_line().encode(
    x=alt.X("yearID"),
    y=alt.Y("sum_salary"),
            color = alt.Color("teamID", scale=alt.Scale(scheme='category10')
    ),
).interactive()
was
# %%
atl = alt.Chart(atl_salary).mark_line().encode(
    x=alt.X("yearID", title = 'Year'),
    y=alt.Y("sum_salary", title = 'Total Salary per year'),
    color = alt.Color("teamID", scale=alt.Scale(scheme='category10')
    ),
).interactive()
atl
# %%
was_and_atl = was + atl
was_and_atl
was_and_atl.save("./was_atl_salary.png")
# %%
