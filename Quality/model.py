from enum import auto
import pandas as pd
import numpy as np

df = pd.read_csv('feat_eng_arahar.csv')
# print(df.columns.tolist())
df = df[[ "Eccentricity" , "eccen_mean" , "MinbyMaj" ,"minby_mean", 'Label',"area","area_mean"]]

from sklearn.model_selection import train_test_split
train_set, test_set  = train_test_split(df, test_size=0.2)

train_set_feat = train_set[["Eccentricity" , "eccen_mean" , "MinbyMaj" ,"minby_mean","area","area_mean"]]
train_set_label = train_set[['Label']].to_numpy()
test_set_feat = test_set[["Eccentricity" , "eccen_mean" , "MinbyMaj" ,"minby_mean","area","area_mean"]]
test_set_label = test_set[['Label']].to_numpy()


# from sklearn.linear_model import LinearRegression
# from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
# from xgboost import XGBClassifier
# from sklearn.ensemble import ExtraTreesRegressor
# model = LinearRegression()
# model = DecisionTreeRegressor()
model = RandomForestRegressor(
    n_estimators= 100 ,
    max_depth=6,
    n_jobs=-1,
)
model.fit(train_set_feat, np.ravel(train_set_label))

from sklearn.metrics import mean_squared_error
daalpredictions = model.predict(test_set_feat)

mse = mean_squared_error(np.ravel(test_set_label), np.ravel(daalpredictions))
rmse = np.sqrt(mse)
print(rmse)
from joblib import dump, load
dump(model, 'Model.joblib') 

######################################
from sklearn.inspection import permutation_importance
import time

start_time = time.time()
result = permutation_importance(
    model, test_set_feat, n_repeats=10, random_state=42, n_jobs=2
)

elapsed_time = time.time() - start_time
print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")

forest_importances = pd.Series(result.importances_mean, index=feature_names)
print(test_set)
