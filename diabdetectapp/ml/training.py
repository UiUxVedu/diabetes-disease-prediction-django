from joblib import dump
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

df= pd.read_csv(r'C:\Users\91962\Desktop\Django\newproject\diab_detect\diabdetectapp\diabetes (1).csv')

print(df.head())
# Shows the Top 5 record from Dataset.

print(df.info())
# system dataset Info show Karel.

print(df.shape)
# a X b show karto

print(df.describe())
# mean-mode-meadian stdeviation and Percentage cal return karto

print(df.duplicated().sum())
#duplicated values cha sum return Karto

#Analysis
print(df.isna().sum())
# null records cha sum return karto

print(df.nunique().sort_values())
# unique values sort kelya jattat
sns.countplot(x='Outcome',data=df)

"""Feature Selection => Manual"""
x = df.drop(['Pregnancies','Outcome'], axis=1)
##data = data.dropna()
print(type(x))

y = df['Outcome']
print(type(y))

from sklearn.model_selection import train_test_split
#training-testin sathi data split karto.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=1234)
#size of data given to training and testing.
from sklearn.svm import SVC
#from sklearn.ensemble import RandomForestClassifier
# data classify kela jato.
svcclassifier = SVC()
svcclassifier.fit(x_train, y_train)

y_pred = svcclassifier.predict(x_test)
print(y_pred)
# parameter is predicted and passed.

print("=" * 40)
print("==========")
print("Classification Report : ",(classification_report(y_test, y_pred)))
print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
accuracy = accuracy_score(y_test, y_pred)
# formula for accuracy
print("Accuracy: %.2f%%" % (accuracy * 100.0))
# ACC = (accuracy_score(y_test, y_pred) * 100)
# repo = (classification_report(y_test, y_pred))

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("==================")
print("Confusion Matrix :\n",conf_matrix)

# Plot the confusion matrix
plt.figure(figsize=(10, 7))
# confussion matrix create kela jato
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
# it will be shown in plots

from joblib import dump
dump (svcclassifier,"model.joblib")
print("Model saved as model.joblib")
model_path = os.path.join(os.path.dirname(__file__), "model.joblib")
dump(svcclassifier, model_path)

print("Model saved at:", model_path)