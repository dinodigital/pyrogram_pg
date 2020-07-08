from pyrogram import Client, Filters, Message

from helpers.database import create_user
from models import User


@Client.on_message(~Filters.bot & Filters.command("start"))
def start(bot: Client, m: Message):
    tg_id = m.from_user.id
    user = User.get_or_none(tg_id=tg_id)

    if user is None:
        user = create_user(m)

    # Первое сообщение пользователю
    bot.send_message(tg_id, 'Hello!')
