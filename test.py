import pandas as pd
from nohotencoder import encoder

columns = ['A_1','A_2', 'A_3']

df = pd.DataFrame(columns=columns)

df['A_1'] = [1,0,0,0]
df['A_2'] = [0,1,0,0]
df['A_3'] = [0,0,1,0]

print(df)

encoder(df, columns, 'A')

print(df)