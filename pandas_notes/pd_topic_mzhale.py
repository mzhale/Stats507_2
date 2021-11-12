#**Mohammad Zhalechian**
#mzhale@umich.edu 


'''## Missing Values in Pandas

* Panda is flexible with regard to handling missing data
* $NaN$ is the default missing value marker in Pandas
* Pandas provides two functions $insa()$ and $notna()$ to detect missing values

df = pd.DataFrame({'one': [1,2,3], 'two':['a','b','c']})
df2 = df.reindex([0,1,2,3,4])

pd.isna(df2)
pd.notna(df2)
pd.isna(df2['two'])

## Inserting Missing Values 

* We can insert missin values using $None$ or $numpy.nan$.
* Pandas objects provide compatibility between $None$ and $numpy.nan$.

df2.loc[0,'one'] = np.nan 
df2.loc[1,'two'] = None

pd.isna(df2)

## Calculations with Missing Values

* Most of descriptive statistics and computational methods are written 
to account for missing data
* For example:
    * When summing data (e.g., $np.sum()$), missing values will 
    be treated as zero.
    * Cumulative methods like $cumsum()$, $np.mean()$, $cumprod()$ ingnore 
    the missing values be default. We can use $skipna=False$ 
    to override this behavior.


np.sum(df2['one'])
np.mean(df2['one'])

## Filling missing values

* We can fill missing values using several methods
    * Replace missing values with a scalar value using $df.fillna('name')$.
    * Filling the missing values with non-missing values forward or 
    backward using $df.fillna(method = 'pad')$. 
    
df3= df2.copy()
df3.fillna('missing')

df4= df2.copy()
df4.fillna(method = 'pad')
'''

