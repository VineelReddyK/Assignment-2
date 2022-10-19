import pandas as pd
df=pd.read_csv("C:/Users/vinil/Downloads/data.csv")
print('csv file :\n',df.to_string())

#Show the basic statistical description about the data
print('basic statistical description about the data :\n',df.describe())

#Check if the data has null values.
print('checking for null values :\n',df.notnull())

# Replace the null values with the mean
c=df.fillna(value=df.mean(),inplace=False)
print('replacing null values with mean value :\n',c)

#Select at least two columns and aggregate the data using: min, max, count, mean
b=df.groupby('Duration').aggregate({'Duration':['mean','min','max','count']})
d=df.groupby('Pulse').aggregate({'Pulse':['mean','min','max','count']})
print('aggregating using DURATION column',b)
print('aggregating using PULSE column',d)

#Filter the dataframe to select the rows with calories values between 500 and 1000.
f=c.query('Calories>=500 and Calories<=1000')
print('rows with calories values > 500 and pulse < 100 :\n',f)

#Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
g=c.query('Calories>500 and Pulse<100')
print(' rows with calories values > 500 and pulse < 100 :\n ',g)

#. Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”
z='Maxpulse'
df_modified=c.loc[:,c.columns !=z]
print('modified dataframe :\n',df_modified)

#Delete the “Maxpulse” column from the main df dataframe
k=c.drop('Maxpulse',axis=1)
print('after deleting MAXPULSE column from main dataframe : \n',k)

#Convert the datatype of Calories column to int datatype.
c['Calories'] = c['Calories'].astype(int)
print(c['Calories'])
print('calaries column to int :\n',c.dtypes)

#Using pandas create a scatter plot for the two columns (Duration and Calories)
plotting=c.plot.scatter(x='Duration', y='Calories')
print('plotting : \n',plotting)