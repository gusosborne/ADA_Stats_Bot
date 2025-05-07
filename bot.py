##Automatically update discord channel names with stake pool stats (gathered from local data, using Guild Operators scripts/cncli/cardano-cli)
##If output data is empty, channels will be hidden from @everyone
##Active Stake:
##Current Epoch:
##Blocks Assigned:
##Blocks Confirmed:
##Blocks Lost:
##Blocks Remaining:
##Next Epoch Blocks:

import discord
from discord.ext import tasks, commands
import subprocess

TOKEN = 'MY_BOT_TOKEN'  # Replace with your bot token
GUILD_ID = MY_GUILD_ID  # Replace with your Discord server's guild ID

# Mapping of channel ID to bash command
CHANNEL_COMMANDS = {
    CHANNEL_ID1: "/bin/bash stats.sh|head -n2|tail -1",  #Channel_IDnum:Command to run (output is new channel name)
    CHANNEL_ID2: "/bin/bash stats.sh|head -n3|tail -1",  #add as many as you like
    CHANNEL_ID3: "/bin/bash stats.sh|head -n4|tail -1",
    CHANNEL_ID4: "/bin/bash stats.sh|head -n6|tail -1",
    CHANNEL_ID5: "/bin/bash stats.sh|head -n5|tail -1",
    CHANNEL_ID6: "/bin/bash stats.sh|head -n8|tail -1",
    CHANNEL_ID7: "/bin/bash stats.sh|head -n11|tail -1"
}

intents = discord.Intents.default()
intents.guilds = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    rename_channels_loop.start()

async def set_channel_visibility(channel: discord.TextChannel, visible: bool):
    """Show or hide the channel from @everyone."""
    overwrite = channel.overwrites_for(channel.guild.default_role)
    overwrite.read_messages = visible
    try:
        await channel.set_permissions(channel.guild.default_role, overwrite=overwrite)
        print(f"{'Unhid' if visible else 'Hid'} channel '{channel.name}'")
    except Exception as e:
        print(f"Failed to set visibility for channel {channel.id}: {e}")

@tasks.loop(minutes=5)
async def rename_channels_loop():
    guild = bot.get_guild(GUILD_ID)
    if not guild:
        print("Guild not found!")
        return

    for channel_id, command in CHANNEL_COMMANDS.items():
        channel = guild.get_channel(channel_id)
        if not channel:
            print(f"Channel with ID {channel_id} not found.")
            continue

        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            new_name = result.stdout.strip()

            if new_name:
                await channel.edit(name=new_name[:100])  # Limit to 100 chars
                await set_channel_visibility(channel, visible=True)
                print(f"Renamed and unhid channel ID {channel_id} to '{new_name}'")
            else:
                await set_channel_visibility(channel, visible=False)
                print(f"Output empty. Hid channel ID {channel_id}.")

        except subprocess.CalledProcessError as e:
            print(f"Error running command for channel {channel_id}: {e.stderr}")

bot.run(TOKEN)
