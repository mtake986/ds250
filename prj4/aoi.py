#%%
# from msilib.schema import Feature
from tkinter import Y
import pandas as pd
import altair as alt
import numpy as np
from types import GeneratorType
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
# %%
url1 = ("dwellings_ml.csv")
# %%
url2 = ("dwellings_denver.csv")
# %%
mlDF = pd.read_csv(url1)
denverDF = pd.read_csv(url2)
#%%
sub_ml = mlDF.sample(5000)
sub_dat = denverDF.sample(5000)
# %%
h_subset = mlDF.filter(['livearea', 'finbsmnt',
    'basement', 'yearbuilt', 'nocars', 'numbdrm', 'numbaths', 
    'stories', 'yrbuilt', 'before1980']).sample(500)

# %%
# sns.lmplot(data=h_subset, x="livearea", y="yrbuilt", col="before1980", hue="before1980")
sns.lmplot(data=h_subset, x="finbsmnt", y="basement", col="before1980", hue="before1980")
sns.lmplot(data=h_subset, x="yrbuilt", y="basement", col="before1980", hue="before1980")

#%%
# Chart 1 for GQ1
chart = sns.lmplot(data=h_subset, x="finbsmnt", y="basement", col="before1980", hue="before1980")
chart

#%%
# Chart 2 for GQ1
sns.lmplot(data=h_subset, x="livearea", y="basement", col="before1980", hue="before1980")

# %%
sns.pairplot(h_subset, hue = 'before1980')
# %%
corr = h_subset.drop(columns = 'before1980').corr()
sns.heatmap(corr)
# %%
sns.set_theme(style="whitegrid")
# %%
df = sns.load_dataset(h_subset)
# %%
g = sns.catplot(x="yrbuilt", y="basement", hue="before1980",
                capsize=.2, palette="YlGnBu_d", height=6, aspect=.75,
                kind="point", data=h_subset)
g.despine(left=True)
# %%










