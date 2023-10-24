print("Test")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

table_MN = pd.read_html('https://en.wikipedia.org/wiki/Minnesota')

print(f'Total tables: {len(table_MN)}')

table_MN = pd.read_html('https://en.wikipedia.org/wiki/Minnesota', match='United States presidential election results for Minnesota')
len(table_MN)

print(f'Total tables: {len(table_MN)}')

df = table_MN[0]
df.head()

# class battingAverage:
#     def __init__():
#         print("lalalal")
#     def mememe():
#         print("lololo")
