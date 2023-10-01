import discord
from discord.ext import commands


def main():
    # Automatically assign roles

    intents = discord.Intents.default()
    intents.presences = True
    bot = commands.Bot(command_prefix='/', intents=intents)

    streamer_role_name = 'Streamer'

    def add_streamer_role():
        @bot.event
        async def on_member_update(before, after):
            # Check if the user is streaming
            is_streaming_now = any(activity.type == discord.ActivityType.streaming for activity in after.activities)

            # Get the 'Streamer' role
            streamer_role = discord.utils.get(after.guild.roles, name=streamer_role_name)

            if is_streaming_now:
                # Assign the 'Streamer' role if the user is streaming
                await after.add_roles(streamer_role)
            else:
                # Remove the 'Streamer' role if the user is not streaming
                await after.remove_roles(streamer_role)

    # Roles
    def admin():
        return

    def moderator():
        return

    def bots():
        return

    def streamer():
        return

    def supporter():
        return


main()
