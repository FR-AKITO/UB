from Sophia import HANDLER, OWNER_ID
from Sophia.__main__ import Sophia
from pyrogram import *
import asyncio

@Sophia.on_message(filters.command("alive", prefixes=HANDLER))
async def Sophia_Alive(_, message):
    await message.edit("◖⁠⚆⁠ᴥ⁠⚆⁠◗ Loading...")
    await message.edit("Success")
