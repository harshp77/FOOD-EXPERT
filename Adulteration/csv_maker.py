from matplotlib.pyplot import axis
import pandas as pd




df = pd.concat(
    map(pd.read_csv, ['G1-araharclr.csv', 'G2-araharclr.csv' , 'G3-araharclr.csv' , 'G3-2-araharclr.csv']), ignore_index=True)

df = df.drop(["Unnamed: 0"] , axis = 1)
df.to_csv('final-3G-arahar.csv')