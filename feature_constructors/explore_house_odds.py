import pandas as pd

#################
### DATA LIGA ###
#################

data_liga = pd.read_csv('Liga1819.csv')
print(data_liga.columns)

features = ['FTHG', 'FTAG', 'FTR',
            'B365H', 'B365D', 'B365A', 'BWH', 'BWD', 'BWA', 'IWH', 'IWD',
            'IWA', 'PSH', 'PSD', 'PSA', 'WHH', 'WHD', 'WHA', 'VCH', 'VCD', 'VCA',
            'BbMxH', 'BbAvH', 'BbMxD', 'BbAvD', 'BbMxA', 'BbAvA']
data = data_liga[features]

def expected_returns(data, h, d, a, ncol, name_column):
    new_col = data.apply(lambda x: 1/x[h] + 1/x[d] + 1/x[a], axis=1)
    data.insert(loc=ncol, column=name_column, value=new_col)

expected_returns(data, 'B365H', 'B365D', 'B365A', 6, 'B365Ret')
expected_returns(data, 'BWH', 'BWD', 'BWA', 10, 'BWRet')
expected_returns(data, 'IWH', 'IWD', 'IWA', 14, 'IWRet')
expected_returns(data, 'PSH', 'PSD', 'PSA', 18, 'PSRet')
expected_returns(data, 'WHH', 'WHD', 'WHA', 22, 'WHRet')
expected_returns(data, 'VCH', 'VCD', 'VCA', 26, 'VCRet')
expected_returns(data, 'BbMxH', 'BbMxD', 'BbMxA', 27, 'BbMxHRet')
expected_returns(data, 'BbAvH', 'BbAvD', 'BbAvA', 27, 'BbAvHRet')

print(data[['BbAvHRet', 'BbMxHRet']].head(100))