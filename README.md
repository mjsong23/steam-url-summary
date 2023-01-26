# steam-url-summary
Mainly created for personal use. Takes a spreadsheet of steam URLs (e.g. a column from Google Forms), uses regex to pattern match the URLs and extract the Steam App IDs, 
counts the AppIDs, and locally matches the results against a list of AppIDs from Steam's API. Main usecase is to summarize crowdsourced product suggestions from Steam.

Download the steam appid Json file from the following link and place it in the same directory as steamurlsummary.py: http://api.steampowered.com/ISteamApps/GetAppList/v0002/
