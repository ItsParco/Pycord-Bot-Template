import discord
from discord.ext import commands

__all__ = (
    "ExtensionBase"
)


class ExtensionBase(commands.Cog):
    def __init__(self, bot: commands.Bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    def embed_author(self, embed: discord.Embed):
        return embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.display_avatar)
