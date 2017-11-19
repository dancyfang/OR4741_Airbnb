import pandas as pd
import pdb

# read csv to dataframe, dtype = 'unicode' sets all column types to 'object'
df = pd.read_csv('MN.csv', dtype = 'unicode')

# select the columns you are interested in
df = df[['ZipCode','Address',
'LandUse','OwnerType','LotArea','BldgArea','NumBldgs','UnitsRes','UnitsTotal',
'LotFront','BldgFront','AssessLand','AssessTot','YearBuilt','YearAlter1','YearAlter2','ResidFAR','CommFAR','FacilFAR']]

# convert some column types  
#df.convert_objects(convert_numeric = True).dtypes
for c in ['LotArea','BldgArea','NumBldgs','UnitsRes','UnitsTotal',
'AssessLand','AssessTot','YearBuilt','YearAlter1','YearAlter2','LotFront','BldgFront','ResidFAR','CommFAR','FacilFAR']:
	df[c] = df[c].astype('float64')

# zoning according to zipcode
A={'10026','10027','10030','10037','10039'}
df['Central Harlem'] = df['ZipCode'].isin(A)
A={'10001', '10011', '10018', '10019', '10020', '10036','10123','10118','10119','10103','10129'}
df['Chelsea and Clinton'] = df['ZipCode'].isin(A)
A={'10029', '10035'}
df['East Harlem'] = df['ZipCode'].isin(A)
A={'10010', '10016', '10017', '10022'}
df['Gramercy Park and Murray Hill'] = df['ZipCode'].isin(A)
A={'10012', '10013', '10014'}
df['Greenwich Village and Soho'] = df['ZipCode'].isin(A)
A={'10004', '10005', '10006', '10007', '10038', '10280','10281','10282'}
df['Lower Manhattan'] = df['ZipCode'].isin(A)
A={'10002', '10003', '10009'}
df['Lower East Side'] = df['ZipCode'].isin(A)
A={'10021', '10028', '10044', '10065', '10075', '10128'}
df['Upper East Side'] = df['ZipCode'].isin(A)
A={'10023', '10024', '10025','10069'}
df['Upper West Side'] = df['ZipCode'].isin(A)
A={'10031', '10032', '10033', '10034', '10040'}
df['Inwood and Washington Heights'] = df['ZipCode'].isin(A)

# Transfer all the true / false to 1 / 0.
for c in ['Central Harlem','Chelsea and Clinton','East Harlem','Gramercy Park and Murray Hill','Greenwich Village and Soho',
          'Lower Manhattan','Lower East Side','Upper East Side','Upper West Side','Inwood and Washington Heights']:
    df[c] = df[c].astype('int64')

# Zipcode 10463 actually belongs to Bronx so we need to drop it
df = df[df['ZipCode'] != '10463']

# delete address that does not start with numbers
df = df[df['Address'].astype(str).str[0] != ' ']

# get dummy variables
df_dummy = pd.get_dummies(df[['LandUse','OwnerType']])
df = pd.concat([df,df_dummy], axis = 1)

# drop some rows with 0
df = df[(df['LotArea'] > 0) & (df['BldgArea'] > 0) & (df['NumBldgs'] > 0)]

# YearBuilt needs to greater than 0 and less than 2018
df = df[(df['YearBuilt'] > 0) & (df['YearBuilt'] < 2018)]

# AssessLand and AssessTot can't be 0
df = df[(df['AssessLand'] > 0) & (df['AssessTot'] > 0)]  

# Merge YearAlter1 and YearAlter2, then rename YearAlter1 to YearAlter
df.YearAlter1[(df.YearAlter2 > 0) & (df.YearAlter1 < df.YearAlter2)] = df.YearAlter2
df.rename(columns = {'YearAlter1':'YearAlter'}, inplace = True)

# Change Column YearAlter2 to IfAlter, which shows whether the property has been altered
df['YearAlter2'] = 0
df.YearAlter2[(df.YearAlter > 0)] = 1
df.rename(columns = {'YearAlter2':'IfAlter'}, inplace = True)

# drop rows with NA values, note dropna is not an inplace function
df = df.dropna()
