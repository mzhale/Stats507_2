# -*- coding: utf-8 -*-
# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ## Contents
# Add a bullet for each topic and link to the level 2 title header using 
# the exact title with spaces replaced by a dash. 
#
# + [Filling missing values](#Filling-missing-values) 
# + [Missing values in pandas](#Missing-values-in-pandas)

# + [markdown] slideshow={"slide_type": "slide"}
# ## Filling missing values
# ## Zane Zhang  zzenghao@umich.edu

# + [markdown] slideshow={"slide_type": "fragment"}
# > Creat a dataframe with nan value

# + slideshow={"slide_type": "fragment"}
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(5, 3),
    index=["a", "c", "d", "e", "f"],
    columns=["one", "two", "three"],
)

df=df.reindex(["a", "b", "c", "d", "e", "f"])
df

# + [markdown] slideshow={"slide_type": "slide"}
# ## filna() method
# * fillna() can “fill in” NA values with non-NA data in a couple of ways
#     * Replace NA with a scalar value
#     
#     
# **fill the nan value with -1**

# + slideshow={"slide_type": "fragment"}
df.fillna(-1)

# + [markdown] slideshow={"slide_type": "subslide"}
# **fill nan with string**

# + slideshow={"slide_type": "fragment"}
df.fillna("missing")

# + [markdown] slideshow={"slide_type": "slide"}
# ## filna() method
# * fillna() can “fill in” NA values with non-NA data in a couple of ways
#     * Fill gaps forward(method="Pad") or backward(method="bfill")

# + slideshow={"slide_type": "fragment"}
print("fill the data based on the forward data")
print(df.fillna(method="pad"))
print("fill the data based on the backward data")
print(df.fillna(method="bfill"))
# -

# ## Missing values in pandas
# ## Mohammad Zhalechian  mzhale@umich.edu

# * Panda is flexible with regard to handling missing data
# * $NaN$ is the default missing value marker in Pandas
# * Pandas provides two function $insa()$ and $notna()$ to detect missing values

# +
df = pd.DataFrame({'one': [1,2,3], 'two':['a','b','c']})
df2 = df.reindex([0,1,2,3,4])

pd.isna(df2)
pd.notna(df2)
pd.isna(df2['two'])
# -

# ## Inserting Missing Values 
#
# * We can insert missin values using $None$ or $numpy.nan$.
# * Pandas objects provide compatibility between $None$ and $numpy.nan$.

# +
df2.loc[0,'one'] = np.nan 
df2.loc[1,'two'] = None

pd.isna(df2)
# -

# ## Calculations with Missing Values
#
# * Most of descriptive statistics and computational methods are written to account for missing data
# * For example:
#     * When summing data (e.g., $np.sum()$), missing values will be treated as zero.
#     * Cumulative methods like $cumsum()$, $np.mean()$, $cumprod()$ ingnore the missing values be default. We can use $skipna=False$ to override this behavior.

np.sum(df2['one'])
np.mean(df2['one'])

# ## Filling missing values
#
# * We can fill missing values using several methods
#     * Replace missing values with a scalar value using $df.fillna('name')$.
#     * Filling the missing values with non-missing values forward or backward using $df.fillna(method = 'pad')$. 

# +
df3= df2.copy()
df3.fillna('missing')

df4= df2.copy()
df4.fillna(method = 'pad')
# -


