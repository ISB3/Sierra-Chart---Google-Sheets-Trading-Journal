# Sierra-Chart---Google-Sheets-Trading-Journal
Hi everyone,  I just wanted to share with you a Trading Journal for Sierra Chart, since the ones I found online (excel and website) never work, at least with me, I decided to make one. If you want to improve it, I'll be happy to see what you did!

The Python script is to takes all the necessary Values into a CSV file at "C:\SierraBacktest\SavedTradeActivity\Journal.csv", you'll need to change this path to a path of your choice with a blank CSV File.
After that you just have to copy/paste the values into the Trading Journal. 
(PS: I know I could probably do it with fewer lines, but I'm not a python expert and it works so for now it's fine with me. But feel free to show me how to optimize it if you wish.) 

For now the Trading Journal is not fully complete since I only have 1 week of Trading History, but I'll update it over time. 
Don't hesitate to complete it according to your needs, it is very simple.

https://docs.google.com/spreadsheets/d/1ieFc0CW549rquCFY3pZZ06g77fIWN4DIlUC_XiSclWo/edit?usp=sharing

-1- From "Trade Activity Log", go to "Statistics" Tab, then "File" -> "Save Log As" into the default path or one of your choice
-2- Run the Python Script and enter the "Statistics.txt" file location (don't forget to make a blank CSV File and change the path of the Variable "fcsv")
-3- Copy/Paste the Values at the Row2 from the CSV File into the Sheets

![brave_dTulD7aBrU](https://user-images.githubusercontent.com/65797034/162839620-a561e796-6593-4aad-b921-8f6755fb8afb.png)
![brave_kMT0JHoevQ](https://user-images.githubusercontent.com/65797034/162839655-4b3feb92-7124-4d24-85ef-2552455d2997.png)


=======================================================================================================================================================================

The python files for trades is absolutely not finished, all it does is to transform the .txt file when you save "Trades" log into a csv file.
I would like to make it delete the unnecessary columns directly, then round the numbers and finally sort the trades by hours but for the moment I can't.
I'll do an update when I have time to work on it. 

So for now what you need to do:
1- Save "Trades" log from "Trade Activity Log" (File -> Save Log As)
2- Modify the path after "pd.read_csv" into the .py file to match yours
3- Modify the path after "df.to_csv" into the .py file to match what you want
4- Into Excel or Libre Office, delete all columns except "Entry DateTime", "Profit/Loss (C)", "FlatToFlat Max Open Profit (C)" & "FlatToFlat Max Open Loss (C)"
5- Round P&L, MFE, Mae with "https://onlinenumbertools.com/round-a-number"
6- Copy into the Sheets at dData

To have the profits/hour, you need to:
1- Separate the column "Entry Date Time" ("Data -> Text to Columns" for LibreOffice) & keep only the Entry Time (tab + space)
2- Round manually the entry to what you want (if you find a way to round time all at once, pls share it)
3- Format the cell "Time" in the format that you want if necessary
4- Data -> Pivot Table -> Insert or Edit.. -> Current Selection -> Drag Time Column into Row Fields -> Drag P&L column into Data Fields

