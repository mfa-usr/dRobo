# This page authenticates the discord bot
# It also passes through relevant information that should be hidden
# APPLICATION_ID & TOKEN are hidden objects not to be published

import discord

# Specify bot permissions
# Since the bot is an administrator - Specify 'all'
intents = discord.Intents.all()

client = discord.Client(intents=intents)

# application_id = '{APPLICATION_ID}'

@client.event
async def on_ready():
    print(f'Bot is logged in as {client.user}')

# client.run('{TOKEN}')