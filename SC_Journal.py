fname = input("Enter file location: ")
fcsv = "C:\SierraBacktest\SavedTradeActivity\Journal.csv"
fh = open(fname)

#Take All Values useful for our Journal
for line in fh:
    if not line.startswith("Closed Trades Profit/Loss"):
        continue
    pnl = round(float(line.split()[3]))
    pnl = [pnl]
    for line in fh:
        if not line.startswith("Closed Trades Total Profit"):
            continue
        total_profit = round(float(line.split()[4]))
        total_profit = [total_profit]
        for line in fh:
            if not line.startswith("Closed Trades Total Loss"):
                continue
            total_loss = round(float(line.split()[4]))
            total_loss = [total_loss]
            for line in fh:
                if not line.startswith("Equity Peak"):
                    continue
                eq_peak = round(float(line.split()[2]))
                eq_peak = [eq_peak]
                for line in fh:
                    if not line.startswith("Equity Valley"):
                        continue
                    eq_valley = round(float(line.split()[2]))
                    eq_valley = [eq_valley]
                    for line in fh:
                        if not line.startswith("Maximum FlatToFlat Trade Open Profit"):
                            continue
                        mfe = round(float(line.split()[5]))
                        mfe = [mfe]
                        for line in fh:
                            if not line.startswith("Maximum FlatToFlat Trade Open Loss"):
                                continue
                            mae = round(float(line.split()[5]))
                            mae = [mae]
                            for line in fh:
                                if not line.startswith("Total Trades"):
                                    continue
                                tot_trades = round(float(line.split()[5]))
                                tot_trades = [tot_trades]
                                for line in fh:
                                    if not line.startswith("Percent Profitable"):
                                        continue
                                    perc_prof = str(line.split()[2])
                                    perc_prof = round(float(perc_prof[:-1]))
                                    perc_prof = [perc_prof]

#print(f"P&L = {pnl} \nTotal Profit = {total_profit} \nTotal Loss = {total_loss}")
#print(f"Equity Peak = {eq_peak} \nEquity Valley = {eq_valley}")
#print(f"MAE = {mae} \nMFE = {mfe} \nPercent Profitable = {perc_prof} \nTotal Trades = {tot_trades}")
import csv
import numpy as np
import pandas as pd
from pathlib import Path  

#Write the Values into Rows of the CSV file
with open(fcsv, 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(pnl)
    writer.writerow(total_profit)
    writer.writerow(total_loss)
    writer.writerow(eq_peak)
    writer.writerow(eq_valley)
    writer.writerow(mfe)
    writer.writerow(mae)
    writer.writerow(tot_trades)
    writer.writerow(perc_prof)

#Delete the spaces between Rows
csv_table = np.genfromtxt("C:\SierraBacktest\SavedTradeActivity\Journal.csv")
transposed = csv_table.T
np.savetxt("C:\SierraBacktest\SavedTradeActivity\Journal.csv", transposed, fmt="%i")
df = pd.read_csv('C:\SierraBacktest\SavedTradeActivity\Journal.csv').head(8)
df_t = df.T

#Transform Rows into Columns
filepath = Path("C:\SierraBacktest\SavedTradeActivity\Journal.csv")  
filepath.parent.mkdir(parents=True, exist_ok=True)  
df_t.to_csv(filepath) 