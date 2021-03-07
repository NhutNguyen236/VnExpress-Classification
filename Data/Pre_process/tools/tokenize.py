'''
    Tokenizer for any dataframe 
    [x] tokenize all of contents and titles
    [] write the token list to file
'''
# Libs import
import nltk
import pandas as pd
import pickle

def tokenizer(path, file_name):
    excel_data_df = pd.read_excel(path)

    # convert dtframe to list 
    title_list = excel_data_df['Title'].tolist()
    content_list = excel_data_df['Content'].tolist()

    merge_data = title_list + content_list
    tokens_storage = []

    for t in merge_data:
        # Convert dtframe element to str
        title_str = str(t)
        title_tokenize = nltk.word_tokenize(title_str)
        for token in title_tokenize:
            tokens_storage.append(token)    
    # Remove duplicates
    tokens_storage = list(dict.fromkeys(tokens_storage))
    
    # Write list tokens_storage to file
    file_path = './Data/Pre_process/processed_data/EN/tokens/' + file_name
    with open(str(file_name), 'w') as filehandle:
        for listitem in tokens_storage:
            filehandle.write('%s\n' % listitem)

# Excecution code
tokenizer('./Data/Pre_process/processed_data/EN/culture.xls', 'culture.txt')
tokenizer('./Data/Pre_process/processed_data/EN/food.xls', 'food.txt')
tokenizer('./Data/Pre_process/processed_data/EN/industries.xls', 'industries.txt')
tokenizer('./Data/Pre_process/processed_data/EN/sports.xls', 'sports.txt')
tokenizer('./Data/Pre_process/processed_data/EN/trend.xls', 'trend.txt')
