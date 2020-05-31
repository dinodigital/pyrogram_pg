from pyrogram import Message


def handle_username(m: Message):
    """
    Возвращает username или пустую строку, если username не задан
    """
    username = m.from_user.username
    return username if username is not None else ""
