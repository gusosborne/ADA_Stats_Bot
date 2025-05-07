<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
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
<span style="font-weight: bold;">This (stats.sh) will only
work out of the box if you are running the Guild Operators environment!</span><br>
<br>
Install: python3 python3-discord screen<br>
<br>
Replace with your pool_bech32 in stats.sh<br>
Replace TOKEN/GUILD_ID/CHANNEL_IDs in bot.py with your own<br>
<br>
Make sure bot has "Manage Channel" &amp; "Manage Permissions"
privileges on all dynamically named channels<br>
Disable all permissions, except "View Channel", for @everyone<br>
Use audio channels for proper text formatting
(text-channels-will-replace-spaces-with-dashes).<br>
<br>
put bot.py &amp; stats.sh in same directory<br>
<br>
Run: screen <br>
Then run: python3 bot.py (Ctrl a+d to detach)<br>
<br>
&nbsp; ..or run: screen -dmS adabot python3 bot.py<br>
  <br>
  <br>
</body>
</html>
![ADABot-Stats](https://github.com/user-attachments/assets/8be07401-a13b-430a-ae20-f9ecd24eeed1)
