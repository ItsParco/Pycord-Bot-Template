import discord
from discord.ext import commands

from ..import ExtensionBase
from core.loader import load_all_extensions


class Dev(ExtensionBase):

    @commands.command(hidden=True)
    @commands.is_owner()
    async def load(self, ctx: commands.Context, extension: str):
        self.bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded Cogs `cogs.{extension}`")

    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload(self, ctx: commands.Context, extension: str):
        core = ['commands.dev']
        if extension in core:
            error = discord.Embed(
                description="Core extension cannot be unloaded**", color=0xF04A47
            )
            await ctx.send(embed=error)
            return
        self.bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"Unloaded `cogs.{extension}`")

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, extension: str):
        if extension in "all *".split():
            await load_all_extensions(self.bot)
            message = "Reload all extension."
        else:
            self.bot.reload_extension(f"cogs.{extension}")
            message = f"Reload `cogs.{extension}`"
        await ctx.send(message)


def setup(bot: commands.Bot):
    bot.add_cog(Dev(bot))
