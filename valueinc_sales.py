# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 11:22:32 2023

@author: ROHAN
"""

import pandas as pd

# reading csv file with ; seperation
data = pd.read_csv('transaction.csv', sep=';')

data.info()




cost_per_item = data['CostPerItem']

selling_price_per_item = data['SellingPricePerItem']

number_of_item_purchased = data['NumberOfItemsPurchased']




profit_per_item = selling_price_per_item - cost_per_item

profit_per_transaction = profit_per_item * number_of_item_purchased

cost_per_transaction = cost_per_item * number_of_item_purchased

sales_per_transaction = selling_price_per_item * number_of_item_purchased

# markup  is simply profit %
markup = (sales_per_transaction - cost_per_transaction) / cost_per_transaction 



# adding a new column to dataframe
data['CostPerTransaction'] = cost_per_transaction

data['SalesPerTransaction'] = sales_per_transaction

data['ProfitPerTransaction'] = profit_per_transaction

data['Markup'] = round(markup, 2)        #rounding up to 2 decimal places


day = data['Day'].astype(str)    #convert column int to str
month = data['Month'].astype(str)
year = data['Year'].astype(str)



# combining date fields
date = day + '-' + month + '-' + year



# adding date to database
data['date'] = date



# using iloc to view specific column/rows
data.iloc[0]   # views the row with index 0
data.iloc[0:3]   # views the row from index 0 to 3
data.iloc[-5:]   # views the last 5 rows
data.head(5)   # views the first 5 rows
data.iloc[:,2]   # views the all row from 3rd column which is year
data.iloc[4,2]   # views specific cell 5th row and 3rd column



# using split to split the client keywords
split_column = data['ClientKeywords'].str.split(',' , expand = True)



# creating new columns for the split columns in client keywords
data['ClientAge'] = split_column[0]

data['ClientType'] = split_column[1]

data['ClientContractDuration'] = split_column[2]



# using the replace the function
data['ClientAge'] = data['ClientAge'].str.replace('[','')

data['ClientContractDuration'] = data['ClientContractDuration'].str.replace(']','')



# using lower function to change items to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()




# how to merge files

# bringing in new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep = ';')

# merging files
# merge_dataframe = pandas.merge(old_dataframe, new_dataframe, on = 'key')
data = pd.merge(data, seasons, on='Month')




# dropping columns
# df = df.drop('column_name', axis = 1)
# axis = 1 is column and axis = 0 is row 
data = data.drop('ClientKeywords', axis = 1)

# dropping mulitples columns using list
data = data.drop(['Day', 'Month', 'Year'], axis = 1)




# Export into a csv
# Index = Flase means we dont need index as unique id in our new csv file
# because we can use transaction id as unique id
data.to_csv('ValueInc_Cleaned.csv' , index = False)






















