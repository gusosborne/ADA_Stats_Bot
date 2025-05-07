<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
</head>
<body>
# ADA_Stats_Bot<br>
Cardano Stake Pool Stats Discord Bot<br>
<br>
Run on BP (use "screen", for a detached session)<br>
stats.sh will only work out of the box if you are running the Guild
Operators environment!<br>
Install: python3 python3-discord screen<br>
Replace with your pool_bech32 in stats.sh<br>
Replace TOKEN/GUILD_ID/CHANNEL_IDs in bot.py with your own<br>
Make sure bot has "Manage Channel" &amp; "Manage Permissions"
privileges on all dynamically named channels (disable all permissions,
except "View Channel", for @everyone).<br>
Use audio channels for proper text formatting
(text-channels-will-replace-spaces-with-dashes).<br>
put bot.py &amp; stats.sh in same directory<br>
<br>
Run: screen <br>
Then run: python3 bot.py (Ctrl a+d to detach)<br>
&nbsp; ..or run: screen -dmS adabot python3 bot.py<br>
</body>
</html>

