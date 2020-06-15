import numpy as np
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

pokemon_df = pd.read_csv("./pokemon.csv")

# SELECT DATA USING LOC 
pokemon_generation = pokemon_df.loc[0:3, ['#', 'Name', 'Generation']]

#GET DATA FROM POKEMON INDEX NUMBER
pokemon_12 = pokemon_df.loc[12,:]


# SELECT DATA
# print(pokemon_df[['#', 'Name', 'Generation']])

print(pokemon_12)
