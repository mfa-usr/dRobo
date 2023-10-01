#!/usr/bin/env python3

# dRobo.py

import auth
import commands
import log
import messages
import roles
import role_commands
import asyncio
import discord


async def bot_authentication():

    # Specify bot permissions
    # Since the bot is an administrator - Specify 'all'
    intents = discord.Intents.all()

    client = discord.Client(intents=intents)

    startup_message = "Starting dRobo..."
    print(startup_message)

    login_event = asyncio.Event()

    @client.event
    async def on_ready():
        print(f'Bot is logged in as {client.user}')

    try:
        await client.start(auth.token)
    except:
        print('Authentication failed. Check bot token.')

    await login_event.wait()


if __name__ == '__main__':
    asyncio.run(bot_authentication())
    # log.main()
    commands.main()
    messages.main()
    roles.main()
    # role_commands.main()
