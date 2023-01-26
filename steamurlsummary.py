import pandas as pd
import re
import json
import sys
import tkinter
from tkinter import filedialog


# Import URLs from a spreadsheet using file explorer
try:
    tkinter.Tk().withdraw()
    fpath = filedialog.askopenfilename()
    appid = pd.read_excel(fpath, names=['URL'], header=None, dtype=str)
except IOError:
    print("Could not open file. \n")
    sys.exit()
# Pattern match using regex and create columns/URL
pattern = 'store\.steampowered.com\/app\/([0-9.]+)'
app_id = appid['URL'].str.extract(pattern, flags=re.I).value_counts(dropna=True).reset_index(name='Counts')
app_id.columns = ['appid', 'count']
app_id['appid'] = pd.to_numeric(app_id['appid'])
app_id['url'] = '''https://store.steampowered.com/app/''' + app_id['appid'].astype(str)



# Download the appID list from http://api.steampowered.com/ISteamApps/GetAppList/v0002/

# Match the appIDs with product titles and include in dataframe
try:
    with open('download.json', "r", encoding='utf8') as read_file:
        steam_data = json.load(read_file)
        steam_data = pd.DataFrame.from_records(steam_data['applist']['apps'])
        app_id = app_id.merge(steam_data, how='left', on='appid')
        app_id.drop_duplicates(subset=['appid'], keep='last', inplace=True)
except IOError:
    print("Issue with download.json. ")
    sys.exit()

app_id = app_id[['appid', 'url', 'name', 'count']]

# Export to new excel sheet via file dialog
print("File generated. Please choose a filename and location: \n")
try:
    with filedialog.asksaveasfile(mode='w', defaultextension='.xlsx') as fname:
        app_id.to_excel(fname.name, index=False)
except IOError:
    print("Could not save file. \n")
    sys.exit()

