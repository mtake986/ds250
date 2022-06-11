
#%%
from types import GeneratorType
import pandas as pd
import altair as alt
import numpy as np
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
#%%
denver = pd.read_csv('./dwellings_denver.csv')
denver

# %%
ml = pd.read_csv('./dwellings_ml.csv')
ml

# %%
h_subset = ml.filter(['livearea', 'finbsmnt', 
    'basement', 'yearbuilt', 'nocars', 'numbdrm', 'numbaths', 
    'stories', 'yrbuilt', 'before1980']).sample(500)

sns.pairplot(h_subset, hue = 'before1980')

corr = h_subset.drop(columns = 'before1980').corr()
# %%
sns.heatmap(corr)

# %%
x_train, x_test, y_train, y_test = train_test_split(
  ml.filter(['livearea', 'finbsmnt', 'basement']),
  ml.before1980,
  test_size = .25, 
  random_state = 76
)
x_train
# %%
x_test
# %%
y_train
# %%
y_test
# %%
sum(x_train.head(10)) / 10
# %%
# create the model
classifier = DecisionTreeClassifier()
classifier
#%%
# train the model
classifier.fit(x_train, y_train)

#%%
# make predictions
y_predictions = classifier.predict(x_test)

# test how accurate predictions are
metrics.accuracy_score(y_test, y_predictions)
# %%
sub_dat = denver.sample(5000)
sub_dat
# %%
alt.Chart(sub_dat).mark_boxplot().encode(
  x = "gartype",
  y=alt.Y("yrbuilt", 
    scale=alt.Scale(
      zero = False
    )
  ),
)
# %%
x = dwellings_ml.filter(['livearea', 'basement', 'yrbuilt', 'gartype_None'])
y = dwellings_ml['before1980']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .34, random_state =76)