import discord
import asyncio
import requests

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

async def check_steam_guides():
    await client.wait_until_ready()
    channel = client.get_channel(YOUR_CHANNEL_ID)  # Replace with your channel ID
    last_known_guide = None

    while not client.is_closed():
        # Check for new Steam guide here
        # If a new guide is found, post it to the Discord channel
        response = requests.get(YOUR_STEAM_GUIDE_URL)  # Replace with your Steam guide URL
        guide_data = response.json()  # Assuming the data is JSON; adjust as needed

        if guide_data and guide_data != last_known_guide:
            last_known_guide = guide_data
            await channel.send(f'New guide posted: {guide_data["title"]}\n{guide_data["url"]}')
        
        await asyncio.sleep(60 * 10)  # Check every 10 minutes

client.loop.create_task(check_steam_guides())
client.run('MTE5ODMzMjMzNjU1NTY5NjIwOQ.G4TEKS.q9y6YcoJo2bLfSrmHZU4vwmtN4DrsP5AeWehqg')  # Replace with your bot token