import discord
from discord.ext import commands

from ...import ExtensionBase
from localizations.get_locale import get_locale


class Message_Clean(ExtensionBase):

    @discord.slash_command(
        name="purge",
        name_localizations=get_locale(name="purge", item="name"),
        description="Quickly delete bulk messages",
        description_localizations=get_locale(name="purge", item="description")
    )
    @discord.default_permissions(manage_messages=True)
    async def purge(self, ctx: discord.ApplicationContext, amount: int, user: discord.User = None):
        deleted = await ctx.channel.purge(
            limit=amount,
            check=lambda message: not message.pinned and (
                message.author == user) if user else True
        )

        response = get_locale(
            locale=ctx.interaction.locale, name="purge", item="response.success_message")
        await ctx.respond(response.format(len(deleted), amount), ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Message_Clean(bot))
