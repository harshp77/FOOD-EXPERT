from matplotlib.pyplot import axis
import pandas as pd




df = pd.concat(
    map(pd.read_csv, ['G1-100-arahar.csv', 'G2-70-arahar.csv' , 'G3-35-arahar.csv' ]), ignore_index=True)

df = df.drop(["Unnamed: 0"] , axis = 1)
df.to_csv('final-3G-arahar.csv')