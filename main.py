from core.bot import Bot
import asyncio


async def main() -> None:
    async with Bot() as bot:
        await bot.start()

if __name__ == "__main__":
    asyncio.run(main())
