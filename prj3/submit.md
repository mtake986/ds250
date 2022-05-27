# Client Report - [Finding relationships in baseball]
__Course CSE 250__
Masahiro Takechi

## Elevator pitch

think about it later

### GRAND QUESTION 1
#### Write an SQL query to create a new dataframe about baseball players who attended BYU-Idaho. The new table should contain five columns: playerID, schoolID, salary, and the yearID/teamID associated with each salary. Order the table by salary (highest to lowest) and print out the table in your report.

#### ANALYSIS

#### TECHNICAL DETAILS

```python 
q1 = pd.read_sql_query("""
  SELECT cp.playerid, s.yearid, s.teamid, s.salary
  FROM CollegePlaying AS cp
    JOIN Salaries AS s on cp.playerid = s.playerid
  where cp.playerid = 'catetr01' or cp.playerid =  'lindsma01' or cp.playerid = 'stephga01'
  GROUP BY s.yearid
  ORDER BY s.salary DESC
""", con)
q1
```

The output is the chart below. 

| playerID   | schoolID   |   yearID | teamID   |   k_salary |
|:-----------|:-----------|---------:|:---------|-----------:|
| lindsma01  | idbyuid    |     2014 | CHA      |       4000 |
| lindsma01  | idbyuid    |     2012 | BAL      |       3600 |
| lindsma01  | idbyuid    |     2011 | COL      |       2800 |
| lindsma01  | idbyuid    |     2013 | CHA      |       2300 |
| lindsma01  | idbyuid    |     2010 | HOU      |       1625 |
| stephga01  | idbyuid    |     2001 | SLN      |       1025 |
| stephga01  | idbyuid    |     2002 | SLN      |        900 |
| stephga01  | idbyuid    |     2003 | SLN      |        800 |
| stephga01  | idbyuid    |     2000 | SLN      |        550 |
| lindsma01  | idbyuid    |     2009 | FLO      |        410 |
| lindsma01  | idbyuid    |     2008 | FLO      |        395 |
| lindsma01  | idbyuid    |     2007 | FLO      |        380 |
| stephga01  | idbyuid    |     1999 | SLN      |        215 |
| stephga01  | idbyuid    |     1998 | PHI      |        185 |
| stephga01  | idbyuid    |     1997 | PHI      |        150 |

### GRAND QUESTION 2
#### This three-part question requires you to calculate batting average (number of hits divided by the number of at-bats)
##### a. Write an SQL query that provides playerID, yearID, and batting average for players with at least 1 at bat that year. Sort the table from highest batting average to lowest, and then by playerid alphabetically. Show the top 5 results in your report.
##### b. Use the same query as above, but only include players with at least 10 at bats that year. Print the top 5 results.
##### c. Now calculate the batting average for players over their entire careers (all years combined). Only include players with at least 100 at bats, and print the top 5 results.

##### Analysis
later

##### TECHNICAL DETAILS
```python
# code
```

The output is the chart below. 
![](imgs/q2.png)


### GRAND QUESTION 3
#### Pick any two baseball teams and compare them using a metric of your choice (average salary, home runs, number of wins, etc). Write an SQL query to get the data you need, then make a graph in Altair to visualize the comparison.

##### Anylysis
later


##### TECHNICAL DETAILS

```python 
#code 
```