import discord
from discord.ext import commands

import logging
import os


logger = logging.getLogger('bot')


def should_ignore_directory(directory: str, ignore_filename="__ignore__") -> bool:
    return ignore_filename in os.listdir(directory)


def find_extensions_recursively(base_path: str, prefix: str = "cogs") -> list[str]:
    extensions = []

    for root, dirs, files in os.walk(base_path):
        if should_ignore_directory(root):
            dirs[:] = []
            continue

        for file in files:
            if file.startswith('_') or not file.endswith('.py'):
                continue

            relative_path = os.path.relpath(
                os.path.join(root, file), base_path)
            module = os.path.splitext(relative_path.replace(os.sep, "."))[0]
            extensions.append(f"{prefix}.{module}")

    return extensions


async def load_all_extensions(bot: commands.Bot, base_path: str = "cogs"):
    extensions = find_extensions_recursively(base_path)

    for ext in extensions:
        try:
            bot.load_extension(ext)
            file_path = os.path.join(*ext.split(".")) + ".py"
            cog_name = ext.split(".")[-1]
            logger.info(f"Loaded {cog_name} ({file_path})")
        except Exception as e:
            logger.error(f"Failed to load {ext}: {e}")
