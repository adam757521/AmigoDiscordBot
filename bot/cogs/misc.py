import random
from datetime import datetime

import aiohttp
import discord
from discord.ext import commands


class Misc(commands.Cog):
    """
    Represents a misc cog
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def generate_embed(
        self, author: discord.User, title: str, footer: str, description: str
    ):
        return (
            discord.Embed(
                description=description,
                timestamp=datetime.utcnow(),
                color=0xDDA0DD,
            )
            .set_footer(text=footer, icon_url=self.bot.user.avatar_url)
            .set_author(name=title, icon_url=author.avatar_url)
        )

    @commands.command(description="Says the text")
    async def say(self, ctx, *, test: commands.clean_content):
        await ctx.send(test)

    @commands.command(description="Finds the member's dick length")
    async def dicklength(self, ctx, member: discord.Member):
        await ctx.send(
            embed=self.generate_embed(
                ctx.author,
                "Dick length calculator!",
                f"Dick length calculated by {self.bot.user}",
                f"{member.mention}'s dick is {random.randint(0, 30)} cm long!",
            )
        )

    @commands.command(description="Shows the ping to the discord websocket")
    async def ping(self, ctx):
        await ctx.send(
            f"Pong! :ping_pong: ping is {round(self.bot.ws.latency * 1000)}."
        )

    @commands.command(description="Calculates the member's gay percentage")
    async def gaycalculate(self, ctx, member: discord.Member):
        gay_percentage = random.randint(0, 100)

        embed = self.generate_embed(
            ctx.author,
            "Gay calculator!",
            f"Gay calculated by {self.bot.user}",
            f"{member.mention} is {gay_percentage}% gay! :rainbow_flag:",
        )

        if gay_percentage > 90:
            embed.description += "\nwow you kinda gay :flushed:"

        await ctx.send(embed=embed)

    @commands.command(aliases=["cv", "coronavirus"], description="Says the covid stats of the country")
    async def covid(self, ctx, *, country: str = "None"):
        country = country.title()

        async with aiohttp.ClientSession() as session:
            datetime_now = datetime.utcnow().strftime("%Y-%m-%d")

            r = await session.get(
                f"https://api.covid19tracking.narrativa.com/api/{datetime_now}/country/{country}"
            )

            r_json = await r.json()

        countries = r_json["dates"][datetime_now]["countries"]

        total = False
        if country not in countries:
            total = True
            information = r_json["total"]
        else:
            information = countries[country]

        embed = self.generate_embed(
            ctx.author,
            f"Coronavirus stats of '{country}'"
            if not total
            else "Total Coronavirus stats",
            f"Coronavirus stats by {self.bot.user}",
            "",
        )

        embed.set_thumbnail(
            url="https://cdn.pixabay.com/photo/2020/05/15/18/46/corona-5174671__340.jpg"
        )
        embed.color = 0x7BF925

        keys = [
            key
            for key in information.keys()
            if "today" in key and "yesterday" not in key
        ]

        for key in keys:
            human_readable = key.replace("_", " ").title()

            embed.add_field(
                name=human_readable, value=str(information[key]), inline=False
            )

        embed.add_field(name="Last Updated", value=r_json["updated_at"], inline=False)

        await ctx.send(embed=embed)

    @commands.command(description="Calculates the sus percentage of the member")
    async def sussycalculator(self, ctx, member: discord.Member):
        sus_dict = {
            90: "You are an Imposter!",
            70: "You are a sussy baka!",
            30: "Susu&Sus",
            0: "You are not an Imposter!",
        }

        sus_percentage = random.randint(0, 100)

        embed = self.generate_embed(
            ctx.author,
            "Sussy calculator!",
            f"Sus calculated by {self.bot.user}",
            f"{member.mention} is {sus_percentage}% sus! 📮",
        )

        for percentage, text in sus_dict.items():
            if sus_percentage >= percentage:
                embed.description += f"\n{text}"
                break

        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Misc(bot))
