import discord
from discord.ext import commands


def main():
    intents = discord.Intents.default()
    intents.presences = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = message.content
        channel = str(message.channel)

        # print(f'{username} said {user_message} in {channel}')

        # Bot responses

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

    print('Messages are running')


main()
