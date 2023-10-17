import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import seaborn as sns
from joblib import dump, load 

df = pd.read_csv("final.csv")
df = df.drop(columns=['Unnamed: 0'])

X=df.iloc[:,:9]
Y=df.iloc[:,9]

from sklearn.model_selection import train_test_split
train_set, test_set  = train_test_split(df, test_size=0.2)

train_set_feat = train_set.iloc[:,:9]
train_set_label = train_set.iloc[:,9].to_numpy()
test_set_feat = test_set.iloc[:,:9]
test_set_label = test_set.iloc[:,9].to_numpy()


model = RandomForestClassifier(n_estimators= 100 ,max_depth=6,n_jobs=-1,)
model.fit(train_set_feat, np.ravel(train_set_label))
# dump(model, 'Color_Model.joblib') 

# y_pred = model.predict(test_set_feat)
# cf_matrix = confusion_matrix(test_set_label, y_pred)

# print(sns.heatmap(cf_matrix, annot=True))