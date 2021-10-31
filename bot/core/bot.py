import logging
import os

import discord
from discord.ext import commands

__all__ = ("AmigoBot",)


class AmigoBot(commands.Bot):
    """
    Represents the core Amigo bot.
    """

    __slots__ = ("token",)

    def __init__(self, token: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = token

    async def on_ready(self):
        print(f"{self.user} is ready.")
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, name="you little sussy bakas"
            ),
            status=discord.Status.idle,
        )

    def load_cogs(self, directory: str) -> None:
        """
        Loads all the cogs in the directory.

        :param str directory: The directory to load.
        :return: None
        :rtype: None
        """

        extension_directory = directory.replace("/", ".")

        path = os.getcwd()
        slash = "/" if "/" in path else "\\"
        for file in os.listdir(path + f"{slash}{directory}"):
            if not file.endswith(".py") or file.startswith("__"):
                continue

            try:
                self.load_extension(f'{extension_directory}.{file.replace(".py", "")}')
                logging.info(f"Loaded cog {file}")
            except Exception as e:
                logging.critical(
                    f"An exception has been raised when loading cog {file}"
                )
                raise e

    def run(self) -> None:
        """
        Runs the bot.

        :return: None
        :rtype: None
        """

        self.load_cogs("bot/cogs")

        super().run(self.token)
