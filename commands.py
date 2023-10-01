import discord
import roles
import selenium
import auth
from discord.ext import commands


def main():
    intents = discord.Intents.default()
    intents.members = True

    bot = commands.Bot(command_prefix='/', intents=intents)

    @bot.command()
    async def check_welcome(ctx, username):
        welcome_channel = discord.utils.get(ctx.guild.text_channels, name='welcome')

        if welcome_channel is None:
            await ctx.send('Welcome channel not found')
            return

        async for message in welcome_channel.history(limit=None):
            if username in message.content:
                # Check if user is still in the server
                user = ctx.guild.get_member_named(username)
                if user is None:
                    # User is not in the server, delete welcome message
                    await message.delete()
                    await ctx.send(f"Deleted welcome message for {username}.")
                    return

        print('Executing')


main()
