from collections import OrderedDict
import inspect

import discord
from discord.ext import commands


def create_parameters_str(parameters: OrderedDict) -> str:
    return " ".join(
        [
            f"[{parameter.name}]"
            if parameter.default is not inspect._empty
            else f"<{parameter.name}>"
            for _, parameter in parameters.items()
        ]
    )


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(description="Shows this message")
    async def help(self, ctx):
        embed = discord.Embed(title="List of Commands", color=0x7BF925)

        for command in self.bot.commands:
            command_with_prefix = f"{self.bot.command_prefix}{command.name}"
            command_arguments = create_parameters_str(command.clean_params)

            embed.add_field(
                name=command_with_prefix,
                value=f"{command_with_prefix} {command_arguments} - {command.description}",
                inline=False,
            )

        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))
