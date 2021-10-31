from discord.ext import commands


class Moderation(commands.Cog):
    """
    Represents a moderation cog
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(description="Clears the amount of messages")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 5):
        await ctx.channel.purge(limit=amount + 1)


def setup(bot: commands.Bot):
    bot.add_cog(Moderation(bot))
