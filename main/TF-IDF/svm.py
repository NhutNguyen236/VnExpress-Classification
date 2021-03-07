import pandas as pd
import numpy as np

excel_data_df = pd.read_excel('./Data/dataset_merged.xls')
content = excel_data_df['Content'].tolist() # data
topic = excel_data_df['Topic'].tolist() # nhãn 

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

#Create the transform
vectorizer1 = TfidfVectorizer()
#Tokenize and build vocab
vectorizer1.fit(content)
#Summarize
new_content = []
new = []
for i in content:
    new_content = i.split()
    temp = [] 
    for j in new_content:
        tong = 1
        for k in j:
            orck = ord(k)
            tong = tong / orck + 1
        temp.append(tong)
    new.append(temp[0:12])
print(new)
'''
new = []
for i in content:
    new.append(i.split())

new_content = []
for i in new:
    new_content += i

content_dv = []
for i in new_content:
    content_dv.append(ord(i))

print(content_dv)
'''
# Import train_test_split function
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(new, topic, test_size=0.2,random_state=109)

#Import svm model
from sklearn import svm

#Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Model Accuracy: how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred) * 100)
print(y_pred)
print(y_train)