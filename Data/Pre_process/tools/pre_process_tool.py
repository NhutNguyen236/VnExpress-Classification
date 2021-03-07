'''
    First step in Pre-processing is lowercasing This is for lowercasing all xls files
'''
# Libs import
import pandas as pd 
import os 
import re
from nltk.corpus import stopwords

# get all of files in Data folder
cwd = os.path.abspath('./Data/Raw_Data/EN')
files = os.listdir(cwd)

print(files)

stops = stopwords.words('english')

for file in files:
    if file.endswith('.xls'):
        print(str(file))
        excel_data_df = pd.read_excel('./Data/Raw_Data/EN/' + file)
        # Lowercase String 
        excel_data_df['Title'] = excel_data_df['Title'].str.lower() 
        excel_data_df['Content'] = excel_data_df['Content'].str.lower()
        excel_data_df['Topic'] = excel_data_df['Topic'].str.lower()

        # Remove punctuation
        excel_data_df['Title'] = excel_data_df['Title'].str.replace('[^\w\s]','')
        excel_data_df['Content'] = excel_data_df['Content'].str.replace('[^\w\s]+','')

        # Remove stop words
        excel_data_df['Title'] = excel_data_df['Title'].apply(lambda x: " ".join(x for x in x.split() if x not in stops))
        excel_data_df['Content'] = excel_data_df['Content'].apply(lambda x: " ".join(x for x in x.split() if x not in stops))

        # Save the file 
        save_path = './Data/Pre_process/processed_data/EN/' + file
        print(save_path)
        excel_data_df.to_excel(save_path)