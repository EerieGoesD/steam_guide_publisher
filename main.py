import discord
import asyncio
import requests

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

async def check_steam_guides():
    await client.wait_until_ready()
    channel = client.get_channel(YOUR_CHANNEL_ID)
    last_known_guide = None

    while not client.is_closed():
        response = requests.get(YOUR_STEAM_GUIDE_URL)
        guide_data = response.json() 

        if guide_data and guide_data != last_known_guide:
            last_known_guide = guide_data
            await channel.send(f'New guide posted: {guide_data["title"]}\n{guide_data["url"]}')
        
        await asyncio.sleep(60 * 10)

client.loop.create_task(check_steam_guides())
client.run(os.getenv('DISCORD_TOKEN'))