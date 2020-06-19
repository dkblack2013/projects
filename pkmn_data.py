# They are for data manipulation
import pandas as pd
import numpy as np

pkmn = pd.read_csv("C:/Users/dkbla/PycharmProjects/projects_pc/datasets_121_280_Pokemon.csv")

print(pkmn.head())
pkmn.details()
for i in pkmn:
    if pkmn[Speed] >= 60:
        print(pkmn[Name])
    else:
        print(str(pkmn['Name']) + " isn't fast enough!")
