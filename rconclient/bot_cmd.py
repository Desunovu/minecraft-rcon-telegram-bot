import os

import aiogram.utils.exceptions

from rconclient.telegram_bot import dp, types
from rconclient.client import admins, client

@dp.message_handler()
async def echo(message: types.Message):
    username =message.from_user.username
    print(f'[{username}]: {message.text}')

    if username in admins:
        # await bot.send_message(message.chat.id, message.text)

        client.connect()
        response = client.command(message.text)
        client.disconnect()
        print(response)

        try:
            await message.answer(response)
        except aiogram.utils.exceptions.MessageTextIsEmpty:
            await message.answer('EMPTY ANSWER')
    else:
        print(f'{username} has no rights :^)')
