from faker import Faker as dc

from firebot import bot as firebot

from ..utils import admin_cmd as wtf


@firebot.on(wtf("card"))
async def _firee(fire):
    cyber = dc()
    killer = cyber.name()
    kali = cyber.address()
    chris = cyber.credit_card_full()
    await fire.edit(f"βπππ:-\n`{killer}`\n\nπΈπππ£ππ€π€:-\n`{kali}`\n\nβππ£π:-\n`{chris}`")
