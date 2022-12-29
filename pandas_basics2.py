# what is Pandas ?
# Pandas are mainly used for data analysis and associate manipulation of tabular data in data frames
# Widely used in Data science and machine learning
# used to process huge and real world data
# Numerous tools to support data load into data objects irrespective of their file formats
# used to reshape data sets


import pandas as pd

#df_csv = pd.read_csv('pokemon_data.csv')

df = pd.read_csv("C:/Users/user716/Downloads/pokemon_data.csv")

print(df)

print(df.tail(5))
# print(df.head(5))

df_xlsx = pd.read_excel("C:/Users/user716/Downloads/pokemon_data.xlsx")
print(df_xlsx.head(3))

#df_txt = pd.read_csv('C:/Users/Z004DEYV/PycharmProjects/pythonProject/Pandas/pokemon_data.txt', delimiter='\t')

#print(df_txt.head(5))

df['HP']

#### Read Headers
df.columns

## Read each Column
# selection
print(df[['Name', 'Type 1', 'HP']])

## Read Each Row
print(df.iloc[0:4])

for index, row in df.iterrows():
     #print(index, row)

     print(index, row['Name'])

df.loc[df['Type 1'] == "Grass"]

## Read a specific location (R,C)


print(df.iloc[2,1])

# sort
df.sort_values(['Speed'], ascending=True)

df.sort_values(['Type 1', 'Speed'], ascending=[1,0])

# changes to data

df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df)

# drop a cloumn from df
df = df.drop(columns=['Total'])
print(df)

df['Total'] = df.iloc[:, 4:10].sum(axis=1)

print(df)

#column operations
cols = list(df.columns)
print(cols)
print(df["Name", "Type 1"])

df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

print(df)
df.head(5)


df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

df = df.drop(columns=['Total'])

df['Total'] = df.iloc[:, 4:10].sum(axis=1)

cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

df.head(5)


df.to_csv('D:\\modified.csv', index=False)

df.to_excel('modified.xlsx', index=False)

df.to_csv('modified.txt', index=False, sep='\t')

# filter data

print(df['Type 1'] == 'Grass')
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

print(new_df)

new_df.reset_index(drop=True, inplace=True)

new_df

new_df.to_csv('filtered.csv')

# conditional changes


df.loc[df['Total'] > 500, ['Generation','Legendary']] = ['Test 1', 'Test 2']

print(df)

df = pd.read_csv('modified.csv')

# aggregate statistics


df = pd.read_csv('modified.csv')

df['count'] = 1

df.groupby(['Type 1', 'Type 2']).count()['count']



# working with large amounts of data

new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('modified.csv', chunksize=5):
     results = df.groupby(['Type 1']).count()

     new_df = pd.concat([new_df, results])


pd.dataframe