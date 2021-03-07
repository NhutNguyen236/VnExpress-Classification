import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Turn feature using TF_IDF
excel_data_df = pd.read_excel('./Data/Pre_process/processed_data/VN/doi_song.xls')
data = excel_data_df['Content'].tolist()

#Create the transform
vectorizer1 = TfidfVectorizer()
#Tokenize and build vocab
vectorizer1.fit(data)
#Summarize
print(vectorizer1.vocabulary_)
print(vectorizer1.idf_)
