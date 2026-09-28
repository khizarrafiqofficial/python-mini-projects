# Define a dataframe named 'Bank_df_1' that contains the first and last names for 5 bank clients with IDs = 1, 2, 3, 4, 5
# Assume that the bank got 5 new clients, define another dataframe named 'Bank_df_2' that contains a new clients with IDs = 6, 7, 8, 9, 10
# Let's assume we obtained additional information (Annual Salary) about all our bank customers (10 customers)
# Concatenate both 'bank_df_1' and 'bank_df_2' dataframes
# Merge client names and their newly added salary information using the 'Bank Client ID'
# Let's assume that you became a new client to the bank
# Define a new DataFrame that contains your information such as client ID (choose 11), first name, last name, and annual salary.
# Add this new dataframe to the original dataframe 'bank_df_all'.

import pandas as pd
# Creating a dataframe from a dictionary
# Let's define a dataframe with a list of bank clients with IDs = 1, 2, 3, 4, 5 

raw_data = {'Bank Client ID': ['1', '2', '3', '4', '5'],
            'First Name': ['Ali', 'Ahsan', 'Bilal', 'Maham', 'Saira'], 
            'Last Name': ['Haider', 'Ali', 'Khan', 'Rafiq', 'Naeem']}

Bank_df_1 = pd.DataFrame(raw_data, columns = ['Bank Client ID', 'First Name', 'Last Name'])



# Let's define another dataframe for a separate list of clients (IDs = 6, 7, 8, 9, 10)
raw_data = {
        'Bank Client ID': ['6', '7', '8', '9', '10'],
        'First Name': ['Khizar', 'Afnan', 'Zain', 'Urooj', 'Ayesha'], 
        'Last Name': ['Rafiq', 'Anwar', 'Shafique', 'Akhtar', 'Imran']}
Bank_df_2 = pd.DataFrame(raw_data, columns = ['Bank Client ID', 'First Name', 'Last Name'])



# Let's assume we obtained additional information (Annual Salary) about our bank customers 
# Note that data obtained is for all clients with IDs 1 to 10 
raw_data = {
        'Bank Client ID': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        'Annual Salary [$/year]': [25000, 35000, 45000, 48000, 49000, 32000, 33000, 34000, 23000, 22000]}
bank_df_salary = pd.DataFrame(raw_data, columns = ['Bank Client ID','Annual Salary [$/year]'])



# Let's concatenate both dataframes #1 and #2
# Note that we now have client IDs from 1 to 10
bank_df_all = pd.concat([Bank_df_1, Bank_df_2])



# Let's merge all data on 'Bank Client ID'
bank_df_all = pd.merge(bank_df_all, bank_df_salary, on = 'Bank Client ID')

new_client = {
        'Bank Client ID': ['11'],
        'First Name': ['Mishal'], 
        'Last Name': ['Shabir'],
        'Annual Salary [$/year]' : [1000]}
new_client_df = pd.DataFrame(new_client, columns = ['Bank Client ID', 'First Name', 'Last Name', 'Annual Salary [$/year]'])


new_df = pd.concat([bank_df_all, new_client_df], axis = 0)
print(new_df)