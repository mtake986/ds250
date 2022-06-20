
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
y_predictions
#%%
# test how accurate predictions are
metrics.accuracy_score(y_test, y_predictions)


# %%
############### Day2 ###############

sub_ml = ml.sample(5000)
sub_dat = denver.sample(5000)

alt.Chart(sub_dat).mark_boxplot().encode(
  y = alt.Y("yrbuilt", scale=alt.Scale(zero=False)),
  x = "gartype"
)


# %%


# %% Day Three
import pandas as pd
import altair as alt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

#%%
# Separate the features (X) and targets (Y)
x = ml.filter(["livearea","basement","stories","numbaths", "before1980"])
y = ml[["before1980"]]

print(x)
print(y)
print(x.before1980)

#%% Split the data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y)

#%% 
classifier_DT = DecisionTreeClassifier(max_depth = 4)

# Fit the decision tree
classifier_DT.fit(x_train, y_train)

# Test the decision tree (make predictions)
y_predicted_DT = classifier_DT.predict(x_test)

# Evaluate the decision tree
print("Accuracy:", metrics.accuracy_score(y_test, y_predicted_DT))
# %%
from sklearn import tree
import matplotlib

#%% 
# method 1 - text
print(tree.export_text(classifier_DT))

#%% 
# method 2 - graph
tree.plot_tree(classifier_DT, feature_names=x.columns, filled=True)

# %%
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")

# %%

#%%
x
# %%
alt.Chart(x.sample(500)).mark_circle(size=30).encode(
    x="before1980",
    y="livearea",
)
# %%
# The usual train-test split mumbo-jumbo
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

#%%
x_train, x_test, y_train, y_test = train_test_split(
  ml.filter(['livearea', 'finbsmnt', 'basement']),
  ml.before1980,
  test_size = .25, 
  random_state = 76
)
nb = GaussianNB()
nb.fit(x_train, y_train)
predicted_probas = nb.predict_proba(x_test)

#%%
# The magic happens here
import matplotlib.pyplot as plt
import scikitplot as skplt
# skplt.metrics.plot_roc(y_test, predicted_probas)
plt.show()

# %%
