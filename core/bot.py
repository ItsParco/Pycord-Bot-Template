import discord
from discord.ext import commands

from .loader import load_all_extensions

from dotenv import load_dotenv

import time
import os

load_dotenv()

__all__ = (
    "Bot",
)


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=".",
            intents=discord.Intents.all()
        )

    async def start(self, token: str = os.getenv('token'), *, reconnect: bool = True):
        return await super().start(token, reconnect=reconnect)

    async def setup_hook(self):
        await load_all_extensions(self)
        await self.sync_commands()

    async def on_ready(self):
        self.strat_timestamp = int(time.time())
        await self.wait_until_ready()
        await self.setup_hook()

        print("Bot is ready!")
