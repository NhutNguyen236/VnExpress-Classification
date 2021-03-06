'''
    First step in Pre-processing is lowercasing This is for lowercasing all xls files
'''
import pandas as pd 
import os 
import re

# get all of files in Data folder
cwd = os.path.abspath('./Data/Raw_Data')
files = os.listdir(cwd)

print(files)

for file in files:
    if file.endswith('.xls'):
        excel_data_df = pd.read_excel('./Data/Raw_Data/' + file)
        # Lowercase String 
        excel_data_df['Title'] = excel_data_df['Title'].str.lower() 
        excel_data_df['Content'] = excel_data_df['Content'].str.lower()
        excel_data_df['Topic'] = excel_data_df['Topic'].str.lower()

        # Remove punctuation
        excel_data_df['Title'] = excel_data_df['Title'].str.replace('[^\w\s]','')
        excel_data_df['Content'] = excel_data_df['Content'].str.replace('[^\w\s]+','')

        # Save the file 
        save_path = './Data/Pre_process/processed_data/' + file
        print(save_path)
        excel_data_df.to_excel(save_path)