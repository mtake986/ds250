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
from sklearn.datasets import make_classification
from sklearn import datasets

#%%
denver = pd.read_csv('./dwellings_denver.csv')
denver

# %%
ml = pd.read_csv('./dwellings_ml.csv')
ml

iris = datasets.load_iris()

iris


# %%
print(iris.feature_names)
# %%
print(iris.target)
print(iris.target_names)
# %%

x = iris.data
y = iris.target

print(x)
print(y)
#%%
x.shape
y.shape

# %%
cif = RandomForestClassifier()
cif.fit(x, y)
# %%
print(cif.feature_importances_)
print(iris.feature_names)
# %%

x.shape
x[0]

# %%
print(cif.predict([[5.1, 3.5, 1.4, 0.2]]))
print(cif.predict_proba(x[[0]]))
# %%
cif.fit(iris.data, iris.target_names[iris.target])
# %%
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2)
# %%
print(x_train.shape, y_train.shape)
# %%
cif.fit(x_train, y_train)
# %%
print(cif.predict([[5.1, 3.5, 1.4, 0.2]]))
print(cif.predict_proba(x[[0]]))

# %%
print(cif.predict(x_test))

# %%
cif.fit(iris.data, iris.target_names[iris.target])

# %%
print(y_test)
# %%
print(cif.score(x_test, y_test))


########### ml data ##########
# %%
ml_subset = ml.filter(['livearea', 'finbsmnt', 
    'basement', 'yearbuilt', 'nocars', 'numbdrm', 'numbaths', 
    'stories', 'yrbuilt', 'before1980']).sample(500)
ml.columns
#%%
x = ml_subset.filter(['livearea', 'finbsmnt', 
    'basement', 'yearbuilt', 'nocars', 'numbdrm', 'numbaths', 
    'stories', 'yrbuilt', 'before1980'])
y = ml_subset[["before1980"]]
x2 = ml_subset.filter(["livearea","nocars","yearbuilt"])
print(x.shape, y.shape)
#%%

x_train, x_test, y_train, y_test = train_test_split(
  x,
  y,
  test_size = .25, 
  random_state = 10
)

#%%
x_train.shape

#%%
classifier = DecisionTreeClassifier()

# %%
classifier.fit(x_train, y_train)

#%%
y_predictions = classifier.predict(x_test)
# %%
metrics.accuracy_score(y_test, y_predictions)
#%%
from sklearn import tree
import matplotlib

#%%
# Create a decision tree
classifier_DT = DecisionTreeClassifier(max_depth = 4)

# Fit the decision tree
classifier_DT.fit(x_train, y_train)

# Test the decision tree (make predictions)
y_predicted_DT = classifier_DT.predict(x_test)

# Evaluate the decision tree
print("Accuracy:", metrics.accuracy_score(y_test, y_predicted_DT))
#%% 
# method 1 - text
print(tree.export_text(classifier_DT))

#%% 
# method 2 - graph
tree.plot_tree(classifier_DT, feature_names=x3.columns, filled=True)

#%% 
# Feature importance
classifier_DT.feature_importances_

x.columns
# Index(['livearea', 'basement', 'stories', 'numbaths'], dtype='object')
#%%
feature_df = pd.DataFrame({'features':x3.columns, 'importance':classifier_DT.feature_importances_})
feature_df
# %%

# %%
cr = RandomForestClassifier()
# %%
cr.fit(x_train, y_train)
# %%
y_predictions = cr.predict(x_test)
# %%
metrics.accuracy_score(y_test, y_predictions)
# %%
#%%
# Create a decision tree
classifier_DT = DecisionTreeClassifier(max_depth = 4)

# Fit the decision tree
classifier_DT.fit(x_train, y_train)

# Test the decision tree (make predictions)
y_predicted_DT = classifier_DT.predict(x_test)

# Evaluate the decision tree
print("Accuracy:", metrics.accuracy_score(y_test, y_predicted_DT))

# %%
ml_subset2 = ml.filter(['livearea', 'finbsmnt', 
    'basement', 'yearbuilt', 'nocars', 'numbdrm', 'numbaths', 
    'stories', 'yrbuilt', 'before1980']).sample(5000)
x3 = ml_subset2[[
  'livearea', 'basement', 'yrbuilt']]
x4 = ml.filter(['livearea', 'basement', 'yrbuilt', 'arcstyle_TWO-STORY', 'finbsmnt', 'abstrprd', 'quality_C', 'status_V', 'condition_AVG', 'numbaths', 'arcstyle_ONE-STORY']).sample(2000)
y = ml_subset2[["before1980"]].sample(2000)
x5 = ml.sample(5000)
x5 = x5.drop('parcel', 1)
y5 = ml["before1980"].sample(5000)
x6 = ml
x6 = x6.drop('parcel', 1)
x6 = x6.drop('before1980', 1)
x6 = x6.drop('yrbuilt', 1)
y6 = ml["before1980"]

x7 = ml.filter(["arcstyle_ONE-STORY", "gartype_Att", "quality_C", "livearea", "basement", "stories", "tasp", "netprice", "sprice", "abstrprd", "numbaths", "status_V", "numbdrm"])
y7 = ml["before1980"]

x8 = ml.filter(["arcstyle_ONE-STORY", "gartype_Att", "quality_C", "livearea", "basement", "stories", "tasp", "netprice", "sprice", "abstrprd", "numbaths", "status_V", "numbdrm", "nocars", "smonth", "finbsmnt", "condition_AVG", "deduct", "qualified_U", "arcstyle_MIDDLE UNIT", "syear", "arcstyle_ONE AND HALF-STORY", "arcstyle_END UNIT", "qualified_Q"])
y8 = ml["before1980"]
#%%
x_train, x_test, y_train, y_test = train_test_split(
  x7,
  y7,
  test_size = .25, 
  random_state = 10
)

# %%
# Create a decision tree
classifier= RandomForestClassifier()
# classifier= DecisionTreeClassifier()

# Fit the decision tree
classifier.fit(x_train, y_train)

# Test the decision tree (make predictions)
y_predicted = classifier.predict(x_test)

# Evaluate the decision tree
print("Accuracy:", metrics.accuracy_score(y_test, y_predicted))


# # %%

# # Feature importance
# classifier.feature_importances_

#%%
feature_df = pd.DataFrame({'features':x7.columns, 'importance':classifier.feature_importances_})
feature_df.sort_values(by="importance", inplace=True)
feature_df.to_markdown(index = False)
# %%

#%%
# a confusion matrix
print(metrics.confusion_matrix(y_test, y_predicted))
y_test
#%%
# this one might be easier to read
print(pd.crosstab(y_test, y_predicted, rownames=['True'], colnames=['Predicted'], margins=True))

#%%
# visualize a confusion matrix
# requires 'matplotlib' to be installed
metrics.plot_confusion_matrix(classifier, x_test, y_test)

# %%

# %%
ml[["yrbuilt", "before1980"]][10000:10100]
# %%
