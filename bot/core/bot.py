import discord
import discordSuperUtils

__all__ = ("AmigoBot",)


class AmigoBot(discordSuperUtils.ExtendedClient):
    """
    Represents the core Amigo bot.
    """

    async def on_ready(self):
        print(f"{self.user} is ready.")
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, name="you little sussy bakas"
            ),
            status=discord.Status.idle,
        )
