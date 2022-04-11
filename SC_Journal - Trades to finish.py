import csv
# import numpy as np
import pandas as pd
# from pathlib import Path  

df = pd.read_csv(r'C:\SierraBacktest\SavedTradeActivity\Trades -- APEX-8522 -- 11-04-22.txt')
df.to_csv (r'C:\SierraBacktest\SavedTradeActivity\Trades -- APEX-8522 -- 11-04-22.csv', index = None)