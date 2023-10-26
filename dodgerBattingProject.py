import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

bettsStats = pd.read_html('https://www.baseball-reference.com/players/b/bettsmo01-bat.shtml') #Referencing baseball-reference.com for stats

print(bettsStats)

df = bettsStats


# class battingAverage:
