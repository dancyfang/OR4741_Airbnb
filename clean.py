import pandas as pd 

# read csv to dataframe, dtype = 'unicode' sets all column types to 'object'
df = pd.read_csv('MN.csv', dtype = 'unicode')

# select the columns you are interested in
df = df[['LandUse','OwnerType','LotArea','BldgArea','NumBldgs','UnitsRes','UnitsTotal']]

# drop rows with NA values
#df.dropna(subset = ['LandUse','OwnerType','LotArea','BldgArea','NumBldgs','UnitsRes','UnitsTotal'])
df.dropna()

# convert some column types  
#df.convert_objects(convert_numeric = True).dtypes
for c in ['LotArea','BldgArea','NumBldgs','UnitsRes','UnitsTotal']:
	df[c] = df[c].astype('int64')
	
# drop some rows with 0
df = df[df['LotArea'] > 0 and df['BldgArea'] > 0 and df['NumBldgs'] > 0]