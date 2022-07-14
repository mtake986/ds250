# %%
import pandas as pd 
import altair as alt
import numpy as np

#%%
url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'

#%%
dat = pd.read_csv(url, encoding = "ISO-8859-1", encoding_errors='ignore')
dat = dat[1:]
len(dat)
len(dat.columns)
dat.columns
#%%
original_dt = pd.read_csv(url, encoding = "ISO-8859-1", encoding_errors='ignore')
original_dt = original_dt[1:]
len(original_dt)
original_dt.columns

# %%
# Method checkpoint Q1
seen = dat["Have you seen any of the 6 films in the Star Wars franchise?"]
seen

#%%
"""
Q1
"""
dat.rename(columns = {'RespondentID':'id'}, inplace = True)
dat
# %%
dat.rename(columns = {
  'Have you seen any of the 6 films in the Star Wars franchise?': 'haveSeenAny',  
  'Do you consider yourself to be a fan of the Star Wars film franchise?': 'fan',  
  'Which of the following Star Wars films have you seen? Please select all that apply.': 'WatchedOne',
  'Unnamed: 4': 'WatchedTw',
  'Unnamed: 5': 'WatchedTh',  
  'Unnamed: 6': 'WatchedFr',  
  'Unnamed: 7': 'WatchedFv',  
  'Unnamed: 8': 'WatchedSx',
  'Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.': 'rankOfEpi1',
  'Unnamed: 10': 'rankOfEpi2',
  'Unnamed: 11': 'rankOfEpi3',  
  'Unnamed: 12': 'rankOfEpi4',  
  'Unnamed: 13': 'rankOfEpi5',  
  'Unnamed: 14': 'rankOfEpi6',
  'Please state whether you view the following characters favorably, unfavorably, or are unfamiliar with him/her.': 'likeHan',  
  'Unnamed: 16': 'likeLuke',  
  'Unnamed: 17': 'likeLeia',  
  'Unnamed: 18': 'likeAnakin',
  'Unnamed: 19': 'likeObi',
  'Unnamed: 20': 'likePalpatine',  
  'Unnamed: 21': 'likeDarth',  
  'Unnamed: 22': 'likeLando',  
  'Unnamed: 23': 'likeBoba',
  'Unnamed: 24': 'likeC3P0',
  'Unnamed: 25': 'likeR2D2',
  'Unnamed: 26': 'likeJar',  
  'Unnamed: 27': 'likePadme',
  'Unnamed: 28': 'likeYoda',
  'Which character shot first?': 'shotFirst',
  'Are you familiar with the Expanded Universe?': 'FamiliarExpdUniv',
  'Do you consider yourself to be a fan of the Expanded Universe?æ': 'fanExpdUniv',
  'Do you consider yourself to be a fan of the Star Trek franchise?': 'fanStarTrek',
  "Household Income": "income",
  "Location (Census Region)": "Location_census_region"
}, inplace = True)
dat

qqa#%%
"""
Q2
"""
dat.columns

# %%
print(f"before === \nthe number of rows: {len(dat)}\n==========")

#%%
i = 0
print(dat)
# while i < len(dat):
#   print(dat[i])
#   i += 1
#   if i > 10:
#     break

#%%
"""
Q2
"""
watched = dat.query("haveSeenAny == 'Yes'")

at_least_watched_one = watched.filter(["WatchedOne", "WatchedTw", "WatchedTh", "WatchedFr", "WatchedFv", "WatchedSx"]).dropna(how="all")
len(at_least_watched_one)

# %%
len(at_least_watched_one.query("WatchedOne == 'Star Wars: Episode I  The Phantom Menace'"))
# %%
len(at_least_watched_one.query("WatchedOne == 'Star Wars: Episode I  The Phantom Menace'")) / len(at_least_watched_one)
# %%

# %%
"""
Q3
"""
# 85 percent of men have seen at least one “Star Wars” film compared to 72 percent of women.
pd.crosstab(dat.Gender, dat.haveSeenAny, normalize="index", margins=True).to_markdown(index=False)

# (dat.haveSeenAny == "Yes").groupby(dat.Gender).mean()

# %%
q3 = watched.dropna(how="all", subset=["WatchedOne", "WatchedTw", "WatchedTh", "WatchedFr", "WatchedFv", "WatchedSx"])
len(q3)

#%%
# Of people who have seen a film, men were also more likely to consider themselves a fan of the franchise: 72 percent of men compared to 60 percent of women.
#%%
q3.query("fanStarTrek == 'Yes'")
pd.crosstab(q3.fanStarTrek, q3.Gender, normalize="index", margins=True)
#%%
q3_2 = q3.dropna(subset=["Gender", "fanStarTrek"])
print(len(q3_2))
pd.crosstab(q3_2.fanStarTrek, q3_2.Gender, normalize="index", margins=True).to_markdown(index=False)
#%%
male = q3.query("Gender == 'Male'")
print(len(male))
female = q3.query("Gender == 'Female'")
print(len(female))
#%%
male.query('fanStarTrek == "Yes"')
# %%
secThDt = dat
# %%
# %%
LEN = len(at_least_watched_one)
LEN
#%%
at_least_watched_one

q3_sum1 = {
  'movie_num':['I', 'II', 'III', 'IV', 'V', 'VI'],
  'percent':
          [
            round(len(at_least_watched_one.query("WatchedOne == 'Star Wars: Episode I  The Phantom Menace'")) / LEN, 2), 
            round(len(at_least_watched_one.query("WatchedTw == 'Star Wars: Episode II  Attack of the Clones'")) / LEN,2),
            round(len(at_least_watched_one.query("WatchedTh == 'Star Wars: Episode III  Revenge of the Sith'")) / LEN, 2), 
            round(len(at_least_watched_one.query("WatchedFr == 'Star Wars: Episode IV  A New Hope'")) / LEN, 2), 
            round(len(at_least_watched_one.query("WatchedFv == 'Star Wars: Episode V The Empire Strikes Back'")) / LEN,2), 
            round(len(at_least_watched_one.query("WatchedSx == 'Star Wars: Episode VI Return of the Jedi'")) / LEN,2)
          ]
}
q3_sum1
df_q3_sum1 = pd.DataFrame.from_dict(q3_sum1)
bars = alt.Chart(df_q3_sum1).mark_bar().encode(
    x=alt.X(
      'percent', 
      axis=alt.Axis(format='%'), 
      title='Percentage'
    ),
    y=alt.Y(
      'movie_num', 
      title='Movie Number'
    ),
)
text = bars.mark_text(
  align="left", 
  baseline="middle", 
  dx = 3
).encode(
  text="percent:Q"
)


chart_q3_sum1 = (bars + text).properties()
chart_q3_sum1.save("./imgs/chart_q3_sum1.png")

# %%
"""
Q3 sum2
"""
q3_sum2_parent_dt = watched.dropna(how="any", subset=["WatchedOne", "WatchedTw", "WatchedTh", "WatchedFr", "WatchedFv", "WatchedSx"])
len(q3_sum2_parent_dt)
Q3_SUM2_LEN = len(q3_sum2_parent_dt) # Op: 471 rows
Q3_SUM2_LEN
# %%

q3_sum2 = {
  'movie_num':['I', 'II', 'III', 'IV', 'V', 'VI'],
  'percent':
          [
            round(len(q3_sum2_parent_dt.query("rankOfEpi1 == '1'")) / Q3_SUM2_LEN*100,0), 
            round(len(q3_sum2_parent_dt.query("rankOfEpi2 == '1'")) / Q3_SUM2_LEN*100,0),
            round(len(q3_sum2_parent_dt.query("rankOfEpi3 == '1'")) / Q3_SUM2_LEN*100,0), 
            round(len(q3_sum2_parent_dt.query("rankOfEpi4 == '1'")) / Q3_SUM2_LEN*100,0), 
            round(len(q3_sum2_parent_dt.query("rankOfEpi5 == '1'")) / Q3_SUM2_LEN*100,0), 
            round(len(q3_sum2_parent_dt.query("rankOfEpi6 == '1'")) / Q3_SUM2_LEN*100,0)
          ]
}
q3_sum2
#%%
df_q3_sum2 = pd.DataFrame.from_dict(q3_sum2)
bars = alt.Chart(df_q3_sum2).mark_bar().encode(
    x=alt.X(
      'percent', 
      title='Percentage'
    ),
    y=alt.Y(
      'movie_num', 
      title='Movie Number'
    ),
)
text = bars.mark_text(
  align="left", 
  baseline="middle", 
  dx = 3
).encode(
  text="percent:Q"
)

chart_q3_sum2 = (bars + text).properties()
chart_q3_sum2.save("./imgs/chart_q3_sum2.png")

# %%
"""
Q4
"""
q3

secThDt.fan.replace({"Yes": "1", 'No': "0"}, inplace=True)
secThDt
# %%
# q3["Which character shot first?"].unique()
secThDt['Which character shot first?'].replace({"I don't understand this question": "-1", "Greedo": "1", "Han": "1"}, inplace=True)

secThDt["FamiliarExpdUniv"].replace({"Yes": "1", "No": "0"}, inplace=True)
secThDt["fanExpdUniv"].replace({"Yes": "1", "No": "0"}, inplace=True)
secThDt["fanStarTrek"].replace({"Yes": "1", "No": "0"}, inplace=True)
secThDt["Gender"].replace({"Male": "1", "Female": "0"}, inplace=True)
secThDt
# %%
# secThDt['Location (Census Region)'].unique()
secThDt['Location (Census Region)'].replace(
  {
    'South Atlantic': "0", 
    'West South Central': "1", 
    'West North Central': "2",
    'Middle Atlantic': "3", 
    'East North Central': "4", 
    'Pacific': "5",
    'Mountain': "6", 
    'New England': "7", 
    'East South Central': "8"
  }, 
  inplace=True
)
secThDt

#%%
dat.columns
#%%
# When we use machine learning to predict salary,
# let's only look at people that have seen at least
# one star wars film
starwars = dat.query('haveSeenAny == "Yes"')
starwars
# Discuss - what's a better way to filter out people who haven't seen star wars?
q3.columns

# %%
day3_at_least_watched_one= watched.dropna(how="all", subset=["WatchedOne", "WatchedTw", "WatchedTh", "WatchedFr", "WatchedFv", "WatchedSx"])
day3_at_least_watched_one

#%%
# Format columns for machine learning

# Let's try this first: convert categories to "one-hot" encodings
shot_first_onehot = pd.get_dummies(day3_at_least_watched_one.shotFirst)
shot_first_onehot
#%%

# What the difference between code above, and this? Which one is better?
shot_first_onehot2 = pd.get_dummies(day3_at_least_watched_one.shotFirst, drop_first=True)
shot_first_onehot2

# %%
# 'get_dummies()' can also be used to convert yes/no answers to 0/1

episode_i = pd.get_dummies(day3_at_least_watched_one.WatchedOne)
episode_i

# %%
episode_i.value_counts()
# %%
episode_v = pd.get_dummies(day3_at_least_watched_one.WatchedFv)
episode_v
# %%
two_columns = day3_at_least_watched_one["Age"].str.split("-", expand = True).rename(columns = {0: 'min_age', 1: 'max_age'})
two_columns

#%%
day3_at_least_watched_one2 = pd.concat([day3_at_least_watched_one, two_columns], axis=1)
day3_at_least_watched_one2.min_age.unique()
# ['18', '30', '> 60', '45', nan]
day3_at_least_watched_one2.min_age.value_counts()
"""
45      240
30      207
> 60    192
18      180
"""
#%%
day3_at_least_watched_one2.max_age.unique()
# ['29', '44', None, '60', nan]
day3_at_least_watched_one2.max_age.value_counts()
"""
60    240
44    207
29    180
"""
# %%
day3_at_least_watched_one2.columns
#%%
q4_1 = day3_at_least_watched_one2.drop(columns="Age")
q4_1
# %%
(q4_1
  .min_age.replace({"18": "1", '30': "2", "45": "3", "> 60": "4", np.nan: "0"}, inplace=True)
  )
q4_1.min_age.fillna(0)
q4_1.min_age.value_counts()
# %%
(q4_1
  .max_age.replace({"29": "1", '44': "2", "60": "3", "None": "4", np.nan: "0"}, inplace=True)
  )
q4_1.max_age.value_counts()
q4_1
# %%
q4_1[["min_age", "max_age"]].head(5).to_markdown(index=False)
# %%
q4_1.Education.unique()
# %%
(q4_1
  .Education.replace(
    {
      np.nan: "0",
      "Less than high school degree": "1",
      'High school degree': "2", 
      'Some college or Associate degree': "3", 
      "Bachelor degree": "4", 
      "Graduate degree": "5", 
    }, inplace=True)
  )
q4_1.Education.head(10).to_markdown(index=False)

#%%
# q4_1["Household Income"].unique()
# %%
(q4_1
  ["Household Income"].replace(
    {
      np.nan: "0",
      "$0 - $24,999": "1",
      '$25,000 - $49,999': "2", 
      '$50,000 - $99,999': "3", 
      "$100,000 - $149,999": "4", 
      "$150,000+": "5", 
    }, inplace=True)
  )
q4_1["Household Income"].head(10).to_markdown(index=False)
# %%
q4_1["Household Income"].value_counts()
#%%

# (q4_1
#   .assign(
#     is_rich=[
#       '1'
#       if x == "4" or x == "5" 
#       else '0' 
#       for x in q4_1['Household Income']
#     ], inplace = True).head(10)
# )

q4_1['is_rich'] = ["1" if x == "4" or x == "5" else "0" for x in q4_1['Household Income']]
  
q4_d = q4_1
q4_d[["Household Income", "is_rich"]].head(10).to_markdown(index=False)
# q4_1.is_rich.value_counts()

# %%
q4_d.head(10)
# %%
(q4_d
  ["haveSeenAny"].replace(
    {
      "Yes": "1",
      "No": "0", 
    }, inplace=True)
  )
# %%
q3
# %%
(q3
  ["haveSeenAny"].replace(
    {
      "Yes": "1",
      "No": "0", 
    }, inplace=True)
  )
# %%
q3.head(10)
# %%
q3.WatchedOne.unique()
# %%
(q3
  ["WatchedOne"].replace(
    {
      "Star Wars: Episode I  The Phantom Menace": "1",
      np.nan: "0", 
    }, inplace=True)
  )
#%%
q3["likeYoda"].value_counts()
# %%
(q3
  # .WatchedTw.replace(
  #   {
  #     "Star Wars: Episode II  Attack of the Clones": "1",
  #     np.nan: "0", 
  #   }, inplace=True)
  .replace(
    {
      "Very favorably": "6",
      "Somewhat favorably": "5", 
      "Neither favorably nor unfavorably (neutral)": "4",
      "Unfamiliar (N/A)": "3",
      "Very unfavorably": "1",
      "Somewhat unfavorably": "2",
    }, inplace=True)
  )
q3.head()
# %%
q3.columns
# %%
q3.rename(columns = {"Which character shot first?": "shotFirst", "Household Income": "income", "Location (Census Region)": "locationCensusRegion"}, inplace=True)
q3
# %%
# (q3
#   .min_age.replace({"18": "1", '30': "2", "45": "3", "> 60": "4", np.nan: "0"}, inplace=True)
#   )
two_columns = q3["Age"].str.split("-", expand = True).rename(columns = {0: 'min_age', 1: 'max_age'})
two_columns

#%%
q3 = pd.concat([q3, two_columns], axis=1)
q3.head()
# %%
(q3
  .Education.replace(
    {
      np.nan: "0",
      "Less than high school degree": "1",
      'High school degree': "2", 
      'Some college or Associate degree': "3", 
      "Bachelor degree": "4", 
      "Graduate degree": "5", 
    }, inplace=True)
  )
# %%
(q3
  ["income"].replace(
    {
      np.nan: "0",
      "$0 - $24,999": "1",
      '$25,000 - $49,999': "2", 
      '$50,000 - $99,999': "3", 
      "$100,000 - $149,999": "4", 
      "$150,000+": "5", 
    }, inplace=True)
  )
# %%
q3['is_rich'] = ["1" if x == "4" or x == "5" else "0" for x in q4_1['Household Income']]
  
# %%
q3.head()
# %%
q3['shotFirst'].replace({"I don't understand this question": "0", "Greedo": "1", "Han": "2"}, inplace=True)

q3["Gender"].replace({"Male": "1", "Female": "0"}, inplace=True)

# %%
# q3['Location (Census Region)'].unique()
q3['locationCensusRegion'].replace(
  {
    'South Atlantic': "0", 
    'West South Central': "1", 
    'West North Central': "2",
    'Middle Atlantic': "3", 
    'East North Central': "4", 
    'Pacific': "5",
    'Mountain': "6", 
    'New England': "7", 
    'East South Central': "8"
  }, 
  inplace=True
)
# q3.drop(columns="Age", inplace=True)
q3.head(5).to_markdown(index=False)
# %%

# %%
len(q3)
# %%
q4_1.shotFirst.unique()
# %%
dat[["shotFirst", "Gender", "Location (Census Region)"]].head()
# %%
"""
q5
"""
watched = dat.query("haveSeenAny == 'Yes'")
q5 = watched.dropna(how="all", subset=["WatchedOne", "WatchedTw", "WatchedTh", "WatchedFr", "WatchedFv", "WatchedSx"])
q5
# %%
shot_first_onehot = pd.get_dummies(q5.shotFirst)
shot_first_onehot.value_counts()
# %%
shot_first_onehot = pd.get_dummies(q5.shotFirst, drop_first=True)
shot_first_onehot.value_counts()
# %%
episode_i = pd.get_dummies(q5.WatchedOne)
episode_i

# %%
episode_i.value_counts()
# %%
two_columns = q5["Age"].str.split("-", expand = True).rename(columns = {0: 'min_age', 1: 'max_age'})

#%%
q5_with_minmaxx_age = pd.concat([q5, two_columns], axis=1)
# %%
(q5_with_minmaxx_age
  .min_age.replace({"18": "1", '30': "2", "45": "3", "> 60": "4", np.nan: "0"}, inplace=True)
  )
(q5_with_minmaxx_age
  .max_age.replace({"29": "1", '44': "2", "60": "3", "None": "4", np.nan: "0"}, inplace=True)
  )
# %%
(q5_with_minmaxx_age
  .Education.replace(
    {
      np.nan: "0",
      "Less than high school degree": "1",
      'High school degree': "2", 
      'Some college or Associate degree': "3", 
      "Bachelor degree": "4", 
      "Graduate degree": "5", 
    }, inplace=True)
  )
# %%
(q5_with_minmaxx_age
  ["income"].replace(
    {
      np.nan: "0",
      "$0 - $24,999": "1",
      '$25,000 - $49,999': "2", 
      '$50,000 - $99,999': "3", 
      "$100,000 - $149,999": "4", 
      "$150,000+": "5", 
    }, inplace=True)
  )
# %%
q5_with_minmaxx_age['is_rich'] = ["1" if x == "4" or x == "5" else "0" for x in q5_with_minmaxx_age['income']]
q5_with_minmaxx_age = q5_with_minmaxx_age.drop(columns="Age")

#%%
q5_with_minmaxx_age.replace(
  {
    'Yes': "1", 
    'No': "0", 
    np.nan: "-1",
  }, 
  inplace=True
)
#%%
q5_with_minmaxx_age["WatchedTw"] = ["-1" if x == "-1" else "1" for x in q5_with_minmaxx_age['WatchedTw']]
q5_with_minmaxx_age["WatchedTh"] = ["-1" if x == "-1" else "1" for x in q5_with_minmaxx_age['WatchedTh']]
q5_with_minmaxx_age["WatchedFr"] = ["-1" if x == "-1" else "1" for x in q5_with_minmaxx_age['WatchedFr']]
q5_with_minmaxx_age["WatchedFv"] = ["-1" if x == "-1" else "1" for x in q5_with_minmaxx_age['WatchedFv']]
q5_with_minmaxx_age["WatchedSx"] = ["-1" if x == "-1" else "1" for x in q5_with_minmaxx_age['WatchedSx']]
#%%
(q5_with_minmaxx_age
  # .WatchedTw.replace(
  #   {
  #     "Star Wars: Episode II  Attack of the Clones": "1",
  #     np.nan: "0", 
  #   }, inplace=True)
  .replace(
    {
      "Very favorably": "6",
      "Somewhat favorably": "5", 
      "Neither favorably nor unfavorably (neutral)": "4",
      "Unfamiliar (N/A)": "3",
      "Somewhat unfavorably": "2",
      "Very unfavorably": "1",
    }, inplace=True)
  )
#%%
q5_with_minmaxx_age.head()
# # %%
# shot_first_onehot = pd.get_dummies(q5_with_minmaxx_age.shotFirst)
# shot_first_onehot.value_counts()
# # %%
# shot_first_onehot = pd.get_dummies(q5.shotFirst, drop_first=True)
# shot_first_onehot.value_counts()
# # %%
# episode_i = pd.get_dummies(q5.WatchedOne)
# episode_i

#%%
q5_with_minmaxx_age_COPY = q5_with_minmaxx_age
q5_with_minmaxx_age_COPY
# %%
q5_with_minmaxx_age_COPY['shotFirst'].replace({"I don't understand this question": "0", "Greedo": "1", "Han": "2"}, inplace=True)

q5_with_minmaxx_age_COPY["Gender"].replace({"Male": "1", "Female": "0"}, inplace=True)

# %%
# q5_with_minmaxx_age_COPY['Location (Census Region)'].unique()
q5_with_minmaxx_age_COPY['Location_census_region'].replace(
  {
    'South Atlantic': "0", 
    'West South Central': "1", 
    'West North Central': "2",
    'Middle Atlantic': "3", 
    'East North Central': "4", 
    'Pacific': "5",
    'Mountain': "6", 
    'New England': "7", 
    'East South Central': "8"
  }, 
  inplace=True
)
# %%
q5_with_minmaxx_age_COPY.head()
# %%
x = q5_with_minmaxx_age_COPY.drop(['income'], axis = 1)
# y = (q5_with_minmaxx_age_COPY.income > 50000) / 1

x.head()

x.columns

#%%
x = q5_with_minmaxx_age_COPY.filter(['fan', 'likeAnakin', 'likeObi', 'likePalpatine', 'likeJar',
       'likePadme', 'likeYoda', 'shotFirst','Education', 'Location_census_region',
       'max_age'])

y = q5_with_minmaxx_age_COPY["income"]

#%%
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
#%%
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .25, random_state = 376)
#%%
# create the model
classifier = RandomForestClassifier()

# train the model
classifier.fit(x_train, y_train)

# make predictions
y_predictions = classifier.predict(x_test)

# test how accurate predictions are
metrics.accuracy_score(y_test, y_predictions)

# %%
classifier.feature_importances_

#%%
feature_df = pd.DataFrame({'features':x.columns, 'importance':classifier.feature_importances_})
feature_df
# %%
bars = alt.Chart(feature_df).mark_bar().encode(
    x="importance",
    # y="features", sort='-x',
    y=alt.Y("features", sort='-x')
)
bars
bars.save("./imgs/feature_importances.png")
# %%
