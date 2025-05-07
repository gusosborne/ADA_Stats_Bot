# ADA_Stats_Bot
Cardano Stake Pool Stats Discord Bot

Run on BP (use "screen", for a detached session)
stats.sh will only work out of the box if you are running the Guild Operators environment!
Install: python3 python3-discord screen
Replace with your pool_bech32 in stats.sh
Replace BOT_TOKEN/GUILD_ID/CHANNEL_IDs in bot.py with your own
Make sure bot has "Manage Channel" & "Manage Permissions" privileges on all dynamically named channels (disable all permissions, except "View Channel", for @everyone).
Use audio channels for proper text formatting (text-channels-will-replace-spaces-with-dashes).
put bot.py & stats.sh in same directory

Run: screen 
Then run: python3 bot.py (Ctrl a+d to detach)
  ..or run: screen -dmS adabot python3 bot.py

