import discord
import discordSuperUtils

import bot


def main():
    amigo_bot = bot.AmigoBot(
        bot.Account.TOKEN, command_prefix=".", intents=discord.Intents.all(), help_command=None
    )

    discordSuperUtils.CommandHinter(amigo_bot)
    # Initializes the discordSuperUtils command hinter on the bot.

    amigo_bot.run()


if __name__ == "__main__":
    main()
